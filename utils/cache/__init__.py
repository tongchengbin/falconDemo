'''
添加缓存支持
'''
import redis
import pickle
from utils.conf import settings

cache = redis.Redis(settings.BROKER_URL)
''''原生的缓存'''
class Pcache:
    def set(self,name,val):
        return cache.set(name,pickle.dumps(val))
    def get(self,name):
        s_data=cache.get(name)
        return pickle.loads(s_data) if s_data is not None else None
    def delete(self,name):
        return cache.delete(name)
'''存储对象'''
pcache=Pcache()
