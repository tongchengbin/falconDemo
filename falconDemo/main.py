import falcon
from utils.core.loader import scan_url
from utils.core.middleware import logMiddleware


class App(falcon.API):
    def __init__(self, *args, **kwargs):
        super(App, self).__init__(*args, **kwargs)


middleware = [logMiddleware,]
router = scan_url('falconDemo.urls.urlpatterns')
app = App(middleware=middleware,router=router)
