# -*- coding: utf-8 -*-

import os

class Base:
    APP_ENV = "Base"

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
