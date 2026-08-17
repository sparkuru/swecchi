# shortlinks 路由

根路径：`/sw/shortlinks`。

| 方法 | 相对路径 | 访问 | 用途 |
| --- | --- | --- | --- |
| `POST` | `/` | 私有 | 创建短链 |
| `GET` | `/{code}` | 混合 | 解析并重定向 |
| `GET` | `/{code}/meta` | 私有 | 读取短链元数据 |
| `PATCH` | `/{code}` | 私有 | 修改目标、过期时间或启用状态 |
| `DELETE` | `/{code}` | 私有 | 撤销短链 |

## 创建短链

`POST /sw/shortlinks`

```json
{
  "url": "https://example.com/articles/42",
  "code": "article-42",
  "expires_at": "2027-01-01T00:00:00Z",
  "public": true
}
```

`code` 可省略，由服务生成。`url` 必须是绝对 HTTP(S) URL；`code` 只能包含小写字母、数字和连字符。成功时返回 `201` 和短链资源。

## 跳转

`GET /sw/shortlinks/{code}` 返回 `302 Found` 和 `Location`。不存在、失效或已撤销的短链返回 `404`，不泄露其曾经存在。公开短链不要求认证；私有短链要求创建者身份。
