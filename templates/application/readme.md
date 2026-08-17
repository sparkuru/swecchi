# {{APP_DISPLAY_NAME}}

{{ONE_SENTENCE_PURPOSE}}

## 使用者与入口

- 使用者：{{PRIMARY_USER_OR_CALLER}}
- 根路径：`/sw/{{APP_ID}}`
- 默认访问级别：{{public | private | mixed}}
- 详细接口：见 [routes.md](routes.md)

## 边界

### 负责

- {{DOMAIN_RESOURCE_OR_CAPABILITY_1}}
- {{DOMAIN_RESOURCE_OR_CAPABILITY_2}}
- {{DOMAIN_RESOURCE_OR_CAPABILITY_3}}

### 不负责

- {{EXPLICIT_NON_GOAL_1}}
- {{EXPLICIT_NON_GOAL_2}}

## 数据与依赖

- 数据所有权：{{OWNED_DATA_OR_NONE}}
- 平台能力：{{db, cache, http-client, secrets, jobs, object-storage, or none}}
- 外部依赖：{{EXTERNAL_SERVICE_OR_NONE}}
- 敏感信息：{{SECRET_NAMES_OR_NONE}}；必须通过平台密钥设施读取。

## 运行行为

- 同步/异步：{{SYNCHRONOUS_OR_ASYNCHRONOUS_AND_REASON}}
- 缓存策略：{{CACHE_POLICY_OR_NONE}}
- 限制与保留期：{{INPUT_SIZE_RATE_RETENTION_LIMITS}}

## 实现备注

{{IMPLEMENTATION_NOTES_OR_OPEN_QUESTIONS}}
