import falcon
from utils.core.loader import scan_url
from utils.core.middleware import logMiddleware, authMiddleware
from utils.core.Exceptions import AppError


class App(falcon.API):
    def __init__(self, *args, **kwargs):
        
        super(App, self).__init__(*args, **kwargs)
        self.add_error_handler(AppError, AppError.handle)


middleware = [logMiddleware,authMiddleware]
router = scan_url('falconDemo.urls.urlpatterns')

app = App(middleware=middleware,router=router)
