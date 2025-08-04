

## dev

1. `go mod init sweechi`
2. `go mod tidy`



## tree

```bash
swecchi-server
├── cli    # 应用程序入口
│   └── main.go    # 主入口
├── config
│   └── config.go
├── deploy # 部署相关
│   ├── docker-compose.yml
│   ├── dockerfile
│   └── setup.sh
├── doc    # 文档
│   ├── api.md
│   └── readme.md
├── internal   # 私有应用代码
│   ├── api    # HTTP API 层
│   │   ├── handler
│   │   │   └── handler.go
│   │   ├── middleware # 中间件
│   │   │   └── middleware.go
│   │   └── route  # 路由配置
│   │       └── route.go
│   ├── dto    # 数据传输对象
│   │   ├── request
│   │   │   └── request.go
│   │   └── response
│   │       └── response.go
│   ├── infrastructure # 基础设施层
│   │   ├── cache  # 缓存实现
│   │   │   └── cache.go
│   │   ├── database
│   │   │   └── database.go
│   │   └── external   # 外部服务集成
│   │       └── external.go
│   └── app    # 应用服务层
│       └── app.go
├── pkg    # 可被外部使用的库代码
│   ├── auth   # 认证
│   │   ├── jwt.go
│   │   └── middleware.go
│   ├── database   # 数据库
│   │   └── connection.go
│   ├── logger # 日志
│   │   ├── format.go
│   │   └── logger.go
│   ├── timer  # 定时任务
│   │   └── cron.go
│   └── sparkle.go # 脚手架
├── script
│   ├── build.sh
│   ├── clean.sh
│   └── setup.sh
├── test
│   └── test.sh
├── .gitignore
├── makefile
├── go.mod
├── go.sum
└── readme.md
```

