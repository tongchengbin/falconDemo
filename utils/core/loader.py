import importlib
from falcon.routing import DefaultRouter

def import_string(dotted_path):
    """
    Import a dotted module path and return the attribute/class designated by the
    last name in the path. Raise ImportError if the import failed.
    """
    try:
        module_path, class_name = dotted_path.rsplit('.', 1)
    except ValueError as err:
        raise ImportError("%s doesn't look like a module path" % dotted_path) from err
    
    module = importlib.import_module(module_path)
    
    try:
        return getattr(module, class_name)
    except AttributeError as err:
        raise ImportError('Module "%s" does not define a "%s" attribute/class' % (module_path, class_name)) from err



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
    
    