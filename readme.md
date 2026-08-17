# swecchi

一个由独立应用组成的个人 API 集合。它提供统一的域名、版本前缀、认证和运行基础设施；每个应用则独立拥有自己的路由、数据和文档。

> 这个仓库正处于设计与迁移阶段。目前还没有可启动的平台运行时；`api/telegraph-parser.py` 是一项尚未接入 HTTP 平台的现有工具。

## 路由模型

平台统一以 `/sw` 作为公开 API 前缀。一个应用占用一个一级路由，一级路由之后的路径完全由该应用定义：

```text
/sw/{app}/{app-owned-route...}

/sw/shortlinks/{code}
/sw/rss/game
/sw/rss/image
/sw/tools/hash
/sw/tools/telegraph/archive
/sw/oauth/providers/github/authorize
```

平台不把 `rss`、`tools` 或其他名称视为特殊类型。它只将 `/sw/{app}/**` 分派给已注册的应用；应用可以继续定义任意层级的路由。因此扩展功能时，先判断它是否应归属于现有应用，再决定是否新增一级应用。

## 应用

| 应用 | 路由前缀 | 作用 | 状态 |
| --- | --- | --- | --- |
| [shortlinks](apps/shortlinks/readme.md) | `/sw/shortlinks` | 创建、解析和管理个人短链 | 设计中 |
| [rss](apps/rss/readme.md) | `/sw/rss` | 生成与聚合个人订阅源 | 设计中 |
| [tools](apps/tools/readme.md) | `/sw/tools` | 无状态小工具及可异步执行的任务 | 设计中 |
| [oauth](apps/oauth/readme.md) | `/sw/oauth` | 本平台使用外部 OAuth 身份提供方 | 设计中 |
| [badge](apps/badge/readme.md) | `/sw/badge` | 原动态徽章服务的保留说明 | 历史应用 |

每个应用目录都包含：

- `app.toml`：机器可读的注册信息、运行能力和挂载位置；
- `readme.md`：目的、使用者、边界和数据责任；
- `routes.md`：稳定的路由、参数、示例与错误约定。

新建应用可从 [应用模板](templates/application/USAGE.md) 复制；模板中的 `{{PLACEHOLDER}}` 必须替换或删除，不能作为应用配置提交。

## 平台契约

新增应用前，请先阅读：

- [架构与目录约定](docs/architecture.md)
- [应用注册契约](docs/application-contract.md)
- [HTTP 约定](docs/http-conventions.md)

平台核心只拥有配置、应用加载、认证与权限、速率限制、日志与追踪、错误格式、OpenAPI、数据库/缓存/密钥/后台任务等共享能力。业务路由、领域模型、专属数据迁移和服务文档属于应用本身。

## 演进方式

`shortlinks`、`rss`、`tools` 和 `oauth` 是四个刻意不同的纵向样本：它们分别覆盖重定向与持久化、内容生成与缓存、同步或异步工具任务、以及外部身份授权。先实现这些样本，再只为已经出现的重复需求抽取平台能力；不要预先建立“工具应用”“RSS 应用”等僵硬的继承体系。
