# rss 路由

根路径：`/sw/rss`。首批 feed 为 `game` 与 `image`；它们是同一应用的二级路由，不是独立的平台应用。

| 方法 | 相对路径 | 访问 | 用途 |
| --- | --- | --- | --- |
| `GET` | `/game` | 公开 | 获取游戏主题 RSS |
| `GET` | `/image` | 公开 | 获取图片主题 RSS |
| `POST` | `/feeds/{name}/refresh` | 私有 | 请求刷新指定 feed |
| `GET` | `/feeds/{name}/status` | 私有 | 查看刷新时间、来源和错误状态 |

`GET /sw/rss/game` 返回 `application/rss+xml; charset=utf-8`。它可以提供 `ETag` 与 `Last-Modified`，支持条件请求；缓存未命中时不应同步抓取上游，而是返回最近一次成功生成的内容或明确的暂不可用错误。

`POST /sw/rss/feeds/{name}/refresh` 提交刷新任务，返回 `202`。`name` 必须是已配置的 feed，不能用请求参数临时指定任意抓取 URL。
