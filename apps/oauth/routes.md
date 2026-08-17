# oauth 路由

根路径：`/sw/oauth`。以下接口描述“平台作为客户端”场景。

| 方法 | 相对路径 | 访问 | 用途 |
| --- | --- | --- | --- |
| `GET` | `/providers` | 私有 | 列出已配置的身份提供方 |
| `GET` | `/providers/{provider}/authorize` | 私有 | 发起授权码 + PKCE 流程 |
| `GET` | `/providers/{provider}/callback` | 回调 | 接收提供方回调 |
| `DELETE` | `/providers/{provider}/connection` | 私有 | 断开已授权连接 |

`authorize` 生成一次性的 `state` 和 PKCE challenge 后重定向至提供方。`callback` 必须验证 state、交换授权码并将令牌存入密钥设施；它不在 URL、日志或错误消息中回显授权码和 token。

`provider` 只能是平台配置的提供方标识，例如 `github`；不能让调用者提交任意 OAuth discovery URL。
