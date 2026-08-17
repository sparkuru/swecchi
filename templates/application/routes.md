# {{APP_DISPLAY_NAME}} 路由

根路径：`/sw/{{APP_ID}}`。

## 路由一览

| 方法 | 相对路径 | 访问 | 用途 | 缓存/副作用 |
| --- | --- | --- | --- | --- |
| `{{METHOD}}` | `{{RELATIVE_PATH}}` | `{{public | private}}` | {{SHORT_PURPOSE}} | {{CACHE_OR_SIDE_EFFECT}} |

删除示例行；每个实际路由都必须在此列出。

## {{OPERATION_NAME}}

`{{METHOD}} /sw/{{APP_ID}}{{RELATIVE_PATH}}`

访问：{{public | authenticated | required permission}}。

### 参数

| 位置 | 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| `{{path | query | body | header}}` | `{{PARAMETER_NAME}}` | `{{TYPE}}` | `{{yes | no}}` | {{VALIDATION_AND_SEMANTICS}} |

若没有参数，写“无”。不要保留示例行。

### 请求示例

```http
{{METHOD}} /sw/{{APP_ID}}{{RELATIVE_PATH}} HTTP/1.1
Content-Type: application/json
Authorization: Bearer {{TOKEN_IF_REQUIRED}}

{{REQUEST_JSON_OR_REMOVE_BLOCK}}
```

### 成功响应

- 状态：`{{200 | 201 | 202 | 204 | 3xx}}`
- 类型：`{{application/json | application/rss+xml | other}}`
- 缓存：{{CACHE_HEADER_OR_POLICY}}
- 副作用：{{CREATED_RESOURCE_QUEUED_JOB_REDIRECT_OR_NONE}}

```json
{{RESPONSE_JSON_OR_REMOVE_BLOCK}}
```

### 错误

| 状态 | `error.code` | 出现条件 |
| --- | --- | --- |
| `{{4xx_or_5xx}}` | `{{STABLE_ERROR_CODE}}` | {{WHEN_IT_HAPPENS}} |

遵循平台的 [HTTP 约定](../../docs/http-conventions.md)。
