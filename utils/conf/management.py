'''
控制应用加载
'''
import os
from . import settings
def execute_from_command_line(argv=None):
    """"""
    settings._setup(argv=argv)