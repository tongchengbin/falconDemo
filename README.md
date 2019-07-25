
## FalconDemo
> 数据库开放使用 希望不要违规操作
#### 项目目录
```
─app
│  ├─views      视图函数

├─falconDemo    应用主目录
│
├─logs          日志文件
└─utils         工具类
    ├─cache     缓存操作封装
    │
    ├─conf      应用配置相关
    │
    ├─core      系统组件(包括中间件和异常等)

    │
    ├─db        数据库操作
```

### Start
```
python manage.py
```

#### 使用Celery

启动方式
```
celery -A tasks.celery worker -l info
```


# Todo

- [x] 项目初始化
- [x] 多配置文件加载
- [x] 路由结构化配置
- [x] 使用DBUtils做数据库连接池
- [x] 使用中间件处理请求
- [x] 添加日志系统
- [x] 登录登出
- [x] 身份验证
- [x] 添加缓存模块
- [x] 整合Celery



