# 应用注册契约

每个应用必须有唯一、稳定、由小写字母、数字和连字符组成的 `id`。其公开根路径固定为 `/sw/{id}`，不可由应用自行改写。

新应用从 [应用模板](../templates/application/USAGE.md) 创建。`templates/` 不是 `apps/` 的一部分，模板内的占位符与 `enabled = false` 不会进入应用注册表。

## `app.toml`

```toml
id = "example"
name = "Example"
version = "0.1.0"
mount = "/sw/example"
module = "apps.example.app:create_application"
enabled = false
visibility = "private" # public | private | mixed
capabilities = ["db", "cache"]
docs = ["readme.md", "routes.md"]
```

字段说明：

- `id`：应用身份和一级路由名；重命名即为破坏性 API 变更。
- `module`：未来运行时加载的应用工厂；工厂返回此应用唯一的 router。
- `enabled`：是否允许平台加载。设计文档可以先保留 `false`。
- `visibility`：默认访问面；具体路由可以更严格，不能更宽松。
- `capabilities`：应用需要的平台能力。首批值为 `db`、`cache`、`http-client`、`secrets`、`jobs`、`object-storage`。
- `docs`：必须至少列出 `README.md` 和 `routes.md`，供注册校验和文档聚合使用。

## 应用工厂

实现时，应用工厂接受平台提供的受限上下文，并返回其根 router。应用通过上下文获得声明过的能力，不读取全局单例，不自行创建数据库连接池。

```python
def create_application(context: ApplicationContext) -> APIRouter:
    ...
```

应用必须：

1. 只定义相对根路径；平台负责挂载 `/sw/{id}`。
2. 使用统一的认证、错误和日志中间件。
3. 在变更路由前同步更新 `routes.md`。
4. 为需要存储的应用声明数据所有权和迁移。
5. 将密钥、回调地址和第三方凭据放在平台配置/密钥设施中。

应用不得：

- 注册 `/sw` 以外的普通业务路由；
- 依赖另一个应用的内部模块或数据库表；
- 在 import 阶段发起网络请求或创建后台线程；
- 以未声明的能力访问外部状态。
