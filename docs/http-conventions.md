# HTTP 约定

## 路径与版本

所有平台业务 API 使用 `/sw/{app}` 前缀。应用的内部路径使用小写 kebab-case；资源标识符作为路径参数，筛选和展示选项作为查询参数。

```text
POST /sw/shortlinks
GET  /sw/shortlinks/{code}
GET  /sw/rss/game
POST /sw/tools/telegraph/archive
```

`GET` 不改变服务器状态；创建、转换、提交任务和撤销操作使用 `POST`、`PATCH` 或 `DELETE`。输出为 RSS、重定向或文件时可以不是 JSON，但仍遵循相同的认证、日志与错误原则。

## JSON 与错误

JSON 请求和响应使用 `application/json; charset=utf-8`。成功响应直接返回资源或结果；创建结果使用 `201 Created`，异步任务提交使用 `202 Accepted`。

所有 JSON 错误使用：

```json
{
  "error": {
    "code": "invalid_request",
    "message": "`url` must be an absolute HTTP(S) URL",
    "request_id": "req_..."
  }
}
```

错误 `code` 是给程序处理的稳定字段，`message` 可随诊断改善而变化。平台为每个请求生成或透传 `X-Request-ID`。

## 身份与公开性

公开路由必须由应用在 `routes.md` 标为“公开”。未标为公开的路由默认要求平台身份认证。应用可以在已认证基础上声明更细的权限，但不得绕过平台认证机制。

## 文档同步

每个路由条目至少说明方法、相对路径、访问级别、参数、响应、错误、缓存/副作用和一个使用示例。实现、OpenAPI 和 `routes.md` 出现差异时，以修复差异为发布前条件。
