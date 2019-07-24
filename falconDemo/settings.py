# -*- coding: utf-8 -*-

import os

class Base:
    APP_ENV = "Base"

    LOGGING = {'version': 1, 'disable_existing_loggers': False,
               'formatters': {'default': {'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'},
                   'simple': {'format': '[%(asctime)s] [%(levelname)s] %(message)s'}},
               'handlers': {'console': {'level': 'INFO', 'class': 'logging.StreamHandler', 'formatter': 'default'},
                   'file': {'level': 'INFO', 'class': 'logging.FileHandler',
                            'filename': os.path.join("logs", 'running.log'), 'formatter': 'default'},
                   'celery': {'level': 'INFO', 'encoding': 'utf-8', 'class': 'logging.FileHandler',
                              'filename': os.path.join("logs", 'celery.log'), 'formatter': 'default'}, },
               'loggers': {'running': {'handlers': ['console', 'file'], 'level': 'INFO', 'propagate': True, },
                   'task': {'handlers': ['console', 'celery'], 'level': 'INFO', 'propagate': True, },
                   'falcon': {'handlers': ['console', 'file'], 'level': 'INFO', 'propagate': True, }}
    
               }

class Dev(Base):
    APP_ENV = "Dev"

class Prod(Base):
    APP_ENV = "Prod"

class Pred(Base):
    APP_ENV = "Pred"


class Config(Dev,Pred,Prod):
    def __init__(self):
        self.__base__ = None
        self.__bases__ = None
    
    def __new__(cls, *args, **kwargs):
        # 读取配置
        env = os.environ.get('env')
        for c in cls.__bases__:
            if c.APP_ENV == env:
                return c
        return cls.__base__.__base__.__new__(cls.__base__.__base__, *args, **kwargs)
