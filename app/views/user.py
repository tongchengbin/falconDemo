from utils.viewset import BaseViewSet
from utils.core.auth import generate_token
from utils.conf import settings
from utils.cache import pcache
from utils.core.Exceptions import UnauthorizedError,InvalidParameterError,UserNotExistsError
import logging
logger=logging.getLogger('running')
class UserObj(object):
    def __init__(self,username=None):
        self.username=username
        
        


class UserView(BaseViewSet):
    auth=False
    def on_post(self,req,res):
        username=req.media.get('username')
        password=req.media.get('password')
        if not username or not password:
            raise InvalidParameterError("请填写用户名和密码")
        #todo
        #check password
        if username==password=="admin":
            user=UserObj(username)
            token = generate_token(username, settings.SECRET_KEY)
            user.token=token
            pcache.set(token, user)
            res.body=self.JsonResponse({"token": token})
        else:
            raise UserNotExistsError("用户名或密码错误")
class UserLogOut(BaseViewSet):
    def on_get(self,req,res):
        logger.info("%s 登出"%req.user.username)
        pcache.delete(req.user.token)
        res.body=self.JsonResponse({"msg":"登出成功"})
        