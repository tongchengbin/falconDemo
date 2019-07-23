import falcon
from falconDemo.settings import Config


class App(falcon.API):
    def __init__(self, *args, **kwargs):
        print("start server %s"%Config.APP_ENV)
        super(App, self).__init__(*args, **kwargs)
    



middleware = []
app = App(middleware=middleware)

if __name__ == "__main__":
    from wsgiref import simple_server
    
    httpd = simple_server.make_server("127.0.0.1", 5000, app)
    httpd.serve_forever()