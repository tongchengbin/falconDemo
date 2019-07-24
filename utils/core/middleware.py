'''中间件'''
import logging
logger = logging.getLogger('request')
class LogMiddleware:
    def process_request(self,req,res,*args,**kwargs):
        logger.info("%s:%s:%s:%s" % (req.path, req.method,res.status, req.params))

    def process_resource(self,req,resource,*args,**kwargs):
        
        pass
    def process_response(self,req,res,respirce,*args,**kwargs):
        res.set_cookie('mygithub','https://tongchengbin.github.io/')
        
logMiddleware=LogMiddleware()