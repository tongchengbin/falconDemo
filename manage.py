import sys,os
import falcon
from falconDemo.management import execute_from_command_line
class App(falcon.API):
    def __init__(self, *args, **kwargs):
        super(App, self).__init__(*args, **kwargs)
    
    



if __name__ == "__main__":
    os.environ.setdefault("FALCON_SETTINGS_MODULE", "falconDemo.settings.Dev")
    execute_from_command_line(sys.argv)
    from wsgiref import simple_server
    middleware = []
    app = App(middleware=middleware)
    httpd = simple_server.make_server("127.0.0.1", 5000, app)
    httpd.serve_forever()