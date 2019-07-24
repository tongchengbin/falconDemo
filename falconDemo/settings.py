# -*- coding: utf-8 -*-

import os

class Base:
    APP_ENV = "Base"

    LOGGING = {'version': 1, 'disable_existing_loggers': False,
               'formatters': {'default': {'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'},
                   'simple': {'format': '[%(asctime)s] [%(levelname)s] %(message)s'}},
               'handlers': {'console': {'level': 'INFO', 'class': 'logging.StreamHandler', 'formatter': 'default'},
                    'request':{'level': 'INFO', 'class': 'logging.FileHandler',
                            'filename': os.path.join("logs", 'request.log'), 'formatter': 'default'},
                   'file': {'level': 'INFO', 'class': 'logging.FileHandler',
                            'filename': os.path.join("logs", 'running.log'), 'formatter': 'default'},
                   'celery': {'level': 'INFO', 'encoding': 'utf-8', 'class': 'logging.FileHandler',
                              'filename': os.path.join("logs", 'celery.log'), 'formatter': 'default'}, },
               'loggers': {
                   'request':{'handlers': ['console', 'request'], 'level': 'INFO', 'propagate': True, },
                   'running': {'handlers': ['console', 'file'], 'level': 'INFO', 'propagate': True, },
                   'task': {'handlers': ['console', 'celery'], 'level': 'INFO', 'propagate': True, },
                   'falcon': {'handlers': ['console', 'file'], 'level': 'INFO', 'propagate': True, }}
    
               }
    DATABASES = {'database': 'ssm', 'user': 'ssm', 'password': '123456', 'host': '47.107.75.121', 'port': 3306}
class Dev(Base):
    APP_ENV = "Dev"


class Prod(Base):
    APP_ENV = "Prod"

class Pred(Base):
    APP_ENV = "Pred"


