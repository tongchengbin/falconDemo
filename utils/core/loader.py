import importlib
from falcon.routing import DefaultRouter

from utils.conf import import_string


def scan_url(url_module, root_url=None,router=None):
    if not isinstance(router,DefaultRouter):
        router=DefaultRouter()
    if root_url is None:
        root_url=""
    urlpatterns=import_string(url_module)
    for _url, _class in urlpatterns:
        _url=root_url+_url
        if isinstance(_class,str):
            scan_url(_class, root_url=_url, router=router)
        else:
            router.add_route(_url,_class())
            
    return router
    
    