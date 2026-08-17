# tools 路由

根路径：`/sw/tools`。

| 方法 | 相对路径 | 访问 | 用途 |
| --- | --- | --- | --- |
| `POST` | `/hash` | 私有 | 计算文本或已上传对象的摘要 |
| `POST` | `/telegraph/archive` | 私有 | 提交 Telegraph 页面归档任务 |
| `GET` | `/jobs/{job_id}` | 私有 | 查询工具任务状态与结果 |

## 哈希

`POST /sw/tools/hash`

```json
{"algorithm": "sha256", "text": "hello"}
```

仅支持白名单算法，例如 `sha256` 和 `sha512`。成功时同步返回摘要；不接受 URL 作为隐式下载输入。

## Telegraph 归档

`POST /sw/tools/telegraph/archive`

```json
{"url": "https://telegra.ph/example-01-01"}
```

接口只接受 `https://telegra.ph/` 页面，返回 `202` 与 `job_id`。任务下载图片、保存原始页面与本地化 HTML；失败图片及其原因属于任务结果。成品的存储位置、下载授权、大小上限和过期清理必须在实现前明确，不能沿用 CLI 的“写入当前目录”行为。
