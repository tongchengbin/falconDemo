import falcon
import logging


class ThingsResource(object):

    def __init__(self):
        self.logger = logging.getLogger('falconDemo.app.views' + __name__)

    def on_get(self, req, resp):
        resp.body="hello world"
