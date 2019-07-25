'''把项目根目录添加到环境变量  '''
import sys,os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
#没有配置自动扫描任务 所以需要手动引入 不然不会读取UserTask 里面的任务函数
from . import UserTask