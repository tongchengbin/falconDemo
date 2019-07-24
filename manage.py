import os
import sys

from utils.conf.management import execute_from_command_line

if __name__ == "__main__":
    os.environ.setdefault("FALCON_SETTINGS_MODULE", "falconDemo.settings.Dev")
    execute_from_command_line(sys.argv)
    from wsgiref import simple_server
    from falconDemo import app
    httpd = simple_server.make_server("127.0.0.1", 5000, app)
    httpd.serve_forever()