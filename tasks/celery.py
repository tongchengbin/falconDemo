# -*- coding: utf-8 -*-
from __future__ import absolute_import
from celery import Celery
import os,sys

from utils.conf.management import execute_from_command_line
from utils.conf import settings


os.environ.setdefault("FALCON_SETTINGS_MODULE", "falconDemo.settings.Base")
execute_from_command_line(sys.argv)
app = Celery('demo',broker=settings.BROKER_URL)
# Using a string here means the worker will not have to
# pickle the object when using Windows.

app.config_from_object('utils.conf:settings')


# celery -A demo worker -l info
