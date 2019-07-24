'''中间件'''
import logging

from utils.core.Exceptions import UnauthorizedError
from utils.cache import pcache
logger = logging.getLogger('request')
class LogMiddleware:
    def process_request(self,req,res,*args,**kwargs):
        logger.info("%s:%s:%s:%s" % (req.path, req.method,res.status, req.params))

    def process_resource(self,req,res,resource,*args,**kwargs):
        pass
    def process_response(self,req,res,respirce,*args,**kwargs):
        res.set_cookie('mygithub','https://tongchengbin.github.io/')
        
        
class AuthMiddleware:
    '''访问控制'''
    def process_resource(self,req,res,resource,*args,**kwargs):
        if req.headers.get('TOKEN'):
            token=req.headers.get('TOKEN')
        elif req.params.get('token'):
            token=req.params.get('token')
        else:
            token=req.media.get('token') if req.media else None
        if not resource.auth:
            return None
        if resource.auth and not token:
            raise UnauthorizedError("权限验证失败")
        user=pcache.get(token)
        if not user:
            raise UnauthorizedError("权限验证失败")
        else:
            req.user=user
            

logMiddleware=LogMiddleware()
authMiddleware=AuthMiddleware()