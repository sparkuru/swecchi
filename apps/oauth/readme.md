# oauth

本平台作为 OAuth 客户端接入外部身份提供方的应用。

目标是满足 openid 的前提下，设计自己的 oauth 应用，用作自己不同 app 的快速登录行为。

## 边界

- 拥有 OAuth state、PKCE verifier、令牌元数据、授权绑定和撤销状态。
- 客户端密钥与 refresh token 必须经平台 `secrets` 能力管理，不进入日志、响应或 Git。
- 只处理外部 OAuth/OIDC 登录与连接，不在第一期充当第三方向本平台申请 token 的 OAuth Provider。
- 若未来实现 OAuth/OIDC Provider，标准 `/.well-known/*`、`/authorize`、`/token` 端点可能需由平台保留在 `/sw/oauth` 以外，必须另行设计。

详见 [路由说明](routes.md)。
