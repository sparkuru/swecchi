# -*- coding: utf-8 -*-
# pip install beautifulsoup4 requests

"""
telegraph-parser.py

Usage:
  python telegraph-parser.py "https://telegra.ph/xxx"

Features:
  1) Fetch a telegra.ph page
  2) Parse title as directory name
  3) Extract all <img> src and download them in document order

Notice:
  - For lawful use only. Ensure you have the right to access and use the target page.
"""

import argparse
import html
import os
import re
import sys
import time
from pathlib import Path
from typing import List, Tuple, Dict

import requests
from bs4 import BeautifulSoup  # type: ignore
from concurrent.futures import ThreadPoolExecutor, as_completed


DEFAULT_USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
)


def sanitize_filename(name: str, replacement: str = "_") -> str:
    """Sanitize a title string so it can be safely used as a directory name."""
    # Unescape HTML entities
    name = html.unescape(name).strip()
    # Replace illegal path characters
    name = re.sub(r"[\\/:*?\"<>|]", replacement, name)
    # Collapse invisible whitespaces
    name = re.sub(r"\s+", " ", name).strip()
    # Limit length to avoid excessively long paths
    return name[:180] if len(name) > 180 else name


def fetch_page(url: str, timeout: float, headers: dict[str, str]) -> str:
    resp = requests.get(url, timeout=timeout, headers=headers)
    resp.raise_for_status()
    return resp.text


def _extract_time_text(soup: "BeautifulSoup") -> str:
    """Best-effort time extraction from telegraph-like pages."""
    meta = soup.select_one(
        'meta[property="article:published_time"]'
    ) or soup.select_one('meta[name="article:published_time"]')
    if meta and meta.get("content"):
        return meta.get("content").strip()
    time_tag = soup.select_one(".tl_article_header time") or soup.find("time")
    if time_tag:
        if time_tag.get("datetime"):
            return time_tag.get("datetime").strip()
        if time_tag.text:
            return time_tag.text.strip()
    return ""


def parse_title_and_images(html_text: str) -> Tuple[str, List[str], str]:
    soup = BeautifulSoup(html_text, "html.parser")

    title_text = ""
    # Prefer <title>, fallback to body header h1
    title_tag = soup.find("title")
    if title_tag and title_tag.text:
        title_text = title_tag.text
    else:
        header_h1 = soup.select_one(".tl_article_header h1")
        title_text = header_h1.text if header_h1 else "telegraph"

    # Telegraph body is usually within #_tl_editor; collect all <img> in order
    article = soup.select_one("#_tl_editor") or soup.select_one(".tl_article_content")
    if not article:
        article = soup

    image_urls: List[str] = []
    for img in article.find_all("img"):
        src = (img.get("src") or "").strip()
        if not src:
            continue
        # Normalize protocol-relative URL
        if src.startswith("//"):
            src = "https:" + src
        image_urls.append(src)

    time_text = _extract_time_text(soup)
    return title_text, image_urls, time_text


def ensure_directory(base_dir: Path, title: str) -> Path:
    safe = sanitize_filename(title)
    # Remove trailing brand suffix like " – Telegraph" if present
    safe = re.sub(r"\s*[–-]\s*Telegraph\s*$", "", safe, flags=re.IGNORECASE)
    target = base_dir / safe
    target.mkdir(parents=True, exist_ok=True)
    return target


def download_with_retry(
    url: str,
    dest_path: Path,
    timeout: float,
    headers: dict[str, str],
    retries: int,
    backoff: float,
) -> Path:
    for attempt in range(1, retries + 1):
        try:
            with requests.get(url, stream=True, timeout=timeout, headers=headers) as r:
                r.raise_for_status()
                # Guess extension from response Content-Type
                content_type = r.headers.get("Content-Type", "")
                ext = guess_extension_from_content_type(content_type)
                if ext and dest_path.suffix.lower() != ext:
                    dest_path = dest_path.with_suffix(ext)
                tmp_path = dest_path.with_suffix(dest_path.suffix + ".part")
                with open(tmp_path, "wb") as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        if chunk:
                            f.write(chunk)
                os.replace(tmp_path, dest_path)
                return dest_path
        except Exception:  # noqa: BLE001 - Centralized retry error handling
            if attempt < retries:
                time.sleep(backoff * attempt)
            else:
                raise


def guess_extension_from_content_type(content_type: str) -> str:
    ct = content_type.split(";")[0].strip().lower()
    mapping = {
        "image/jpeg": ".jpg",
        "image/jpg": ".jpg",
        "image/png": ".png",
        "image/webp": ".webp",
        "image/gif": ".gif",
        "image/bmp": ".bmp",
        "application/octet-stream": "",  # unknown
    }
    return mapping.get(ct, "")


def build_headers(user_agent: str | None) -> dict[str, str]:
    headers = {
        "User-Agent": user_agent or DEFAULT_USER_AGENT,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
    }
    return headers


def rewrite_html_with_local_images(
    html_text: str, url_to_local_name: Dict[str, str]
) -> str:
    """Replace <img src> with local filenames if present in mapping."""
    soup = BeautifulSoup(html_text, "html.parser")
    article = (
        soup.select_one("#_tl_editor") or soup.select_one(".tl_article_content") or soup
    )
    for img in article.find_all("img"):
        src = (img.get("src") or "").strip()
        if not src:
            continue
        if src.startswith("//"):
            src = "https:" + src
        local = url_to_local_name.get(src)
        if local:
            img["src"] = local
    return str(soup)


def _normalize_url(url: str) -> str:
    url = (url or "").strip()
    if url.startswith("//"):
        return "https:" + url
    return url


def _guess_dest_path_for_index(
    target_dir: Path, index: int, width: int, img_url: str
) -> Path:
    stem = str(index).zfill(width)
    url_ext_match = re.search(
        r"\.(jpg|jpeg|png|webp|gif|bmp)(?:\?|#|$)", img_url, re.IGNORECASE
    )
    ext = f".{url_ext_match.group(1).lower()}" if url_ext_match else ".jpg"
    return target_dir / f"{stem}{ext}"


def _download_one(
    index: int,
    img_url: str,
    target_dir: Path,
    width: int,
    total_count: int,
    timeout: float,
    headers: dict[str, str],
    retries: int,
    backoff: float,
) -> Tuple[str, str]:
    normalized = _normalize_url(img_url)
    dest = _guess_dest_path_for_index(target_dir, index, width, normalized)
    print(f"[Download] {index}/{total_count} -> {dest.name}")
    final_path = download_with_retry(
        normalized,
        dest,
        timeout=timeout,
        headers=headers,
        retries=retries,
        backoff=backoff,
    )
    return normalized, final_path.name


def download_images_concurrently(
    image_urls: List[str],
    target_dir: Path,
    timeout: float,
    headers: dict[str, str],
    retries: int,
    backoff: float,
    workers: int,
    rounds: int,
) -> Tuple[Dict[str, str], List[Tuple[int, str]]]:
    total_count = len(image_urls)
    width = max(4, len(str(total_count)))

    # Work list keeps (index, url) in document order
    remaining: List[Tuple[int, str]] = list(enumerate(image_urls, start=1))
    url_to_local: Dict[str, str] = {}

    print(f"[Info] Total images: {total_count}")
    for round_idx in range(1, max(1, rounds) + 1):
        if not remaining:
            break
        print(f"[Round] {round_idx} start, remaining: {len(remaining)}")

        next_remaining: List[Tuple[int, str]] = []
        with ThreadPoolExecutor(max_workers=max(1, workers)) as executor:
            future_map = {
                executor.submit(
                    _download_one,
                    index,
                    img_url,
                    target_dir,
                    width,
                    total_count,
                    timeout,
                    headers,
                    retries,
                    backoff,
                ): (index, img_url)
                for index, img_url in remaining
            }

            for future in as_completed(future_map):
                index, img_url = future_map[future]
                try:
                    normalized, local_name = future.result()
                    url_to_local[normalized] = local_name
                except Exception as e:  # noqa: BLE001 - aggregated handling
                    print(f"[Failed] {img_url} -> {e}", file=sys.stderr)
                    next_remaining.append((index, img_url))

        remaining = next_remaining
        if remaining:
            print(f"[Round] {round_idx} done, still failing: {len(remaining)}")

    return url_to_local, remaining


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Parse telegra.ph page and download images in order."
    )
    parser.add_argument("url", help="telegra.ph page URL")
    parser.add_argument(
        "--out",
        dest="out_dir",
        default=".",
        help="Output root directory (default: current)",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=20.0,
        help="Request timeout in seconds (default: 20)",
    )
    parser.add_argument(
        "--retries",
        type=int,
        default=3,
        help="Retry times on download failure (default: 3)",
    )
    parser.add_argument(
        "--backoff",
        type=float,
        default=1.5,
        help="Exponential backoff factor (default: 1.5)",
    )
    parser.add_argument("--ua", dest="ua", default=None, help="Custom User-Agent")
    parser.add_argument(
        "--workers",
        type=int,
        default=8,
        help="Concurrent workers for downloads (default: 8)",
    )
    parser.add_argument(
        "--rounds",
        type=int,
        default=3,
        help="Max rounds to reattempt failed downloads set (default: 3)",
    )

    args = parser.parse_args()

    headers = build_headers(args.ua)

    try:
        html_text = fetch_page(args.url, timeout=args.timeout, headers=headers)
    except Exception as e:
        print(f"[Error] Failed to fetch page: {e}", file=sys.stderr)
        sys.exit(2)

    title_text, image_urls, time_text = parse_title_and_images(html_text)
    if not image_urls:
        print("[Warning] No images found on the page.", file=sys.stderr)

    base_dir = Path(args.out_dir)
    target_dir = ensure_directory(base_dir, title_text)

    # Concurrent download with multi-round retries
    url_to_local, remaining = download_images_concurrently(
        image_urls=image_urls,
        target_dir=target_dir,
        timeout=args.timeout,
        headers=headers,
        retries=args.retries,
        backoff=args.backoff,
        workers=args.workers,
        rounds=args.rounds,
    )

    if remaining:
        # Write failed list to help manual retry if needed
        try:
            failed_path = target_dir / "failed.txt"
            with open(failed_path, "w", encoding="utf-8") as f:
                for index, url in sorted(remaining):
                    f.write(f"{index}\t{url}\n")
            print(
                f"[Warning] {len(remaining)} files still failed after all rounds. See failed.txt",
                file=sys.stderr,
            )
        except Exception as e:
            print(f"[Failed] write failed.txt -> {e}", file=sys.stderr)

    # Write readme.txt with url/title/time
    try:
        readme_path = target_dir / "readme.txt"
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(f"url: {args.url}\n")
            f.write(f"title: {title_text}\n")
            f.write(f"time: {time_text}\n")
    except Exception as e:
        print(f"[Failed] write readme.txt -> {e}", file=sys.stderr)

    # Save rewritten HTML with local image paths
    try:
        # Also make mapping work for protocol-relative URLs
        expanded_map: Dict[str, str] = dict(url_to_local)
        for k, v in list(url_to_local.items()):
            if k.startswith("https://"):
                proto_less = k.replace("https:", "", 1)
                if proto_less.startswith("//"):
                    expanded_map[proto_less] = v
        rewritten = rewrite_html_with_local_images(html_text, expanded_map)
        with open(target_dir / "index.html", "w", encoding="utf-8") as f:
            f.write(rewritten)
    except Exception as e:
        print(f"[Failed] write index.html -> {e}", file=sys.stderr)

    print(f"Done. Found {len(image_urls)} images, output to: {target_dir}")


if __name__ == "__main__":
    main()
