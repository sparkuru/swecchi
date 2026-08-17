# 应用模板使用说明

此目录是新应用的可复制起点，不属于 `apps/`，不会被平台加载。新建应用时：

1. 复制整个目录到 `apps/{{APP_ID}}/`。
2. 替换全部 `{{PLACEHOLDER}}`，并删除不适用的行、示例和章节。
3. 使 `app.toml` 的 `id`、目录名和 `mount` 保持一致：`id = "foo"` 对应 `apps/foo/` 与 `/sw/foo`。
4. 在根 README 的应用表加入该应用，并在 `app.toml` 保持 `enabled = false`，直至实现和文档均准备完成。
5. 实现前后都遵守 [应用注册契约](../../docs/application-contract.md) 与 [HTTP 约定](../../docs/http-conventions.md)。

占位符书写规则：

- `{{ALL_CAPS}}`：必须替换或删除；它表示具体事实、路径、字段或行为。
- `{{a | b}}`：从给出的选项选择一个，不能原样保留。
- `{{... OR NONE}}`：没有对应内容时填写 `none`，不要凭空补功能。

`README.md` 描述用途、边界、数据责任和运行限制；`routes.md` 是 HTTP 契约。不要把所有细节只写在其中一个文件里。
