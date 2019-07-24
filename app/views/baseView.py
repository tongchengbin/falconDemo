import falcon
import logging
from utils.db import POOL
from utils.viewset import BaseViewSet


class ThingsResource(BaseViewSet):

    def __init__(self,db=None):
        self.logger = logging.getLogger('falconDemo.app.views' + __name__)

    def on_get(self, req, resp):
        con = POOL.connection()
        cur = con.cursor()
        cur.execute('select * from user')
        data=cur.fetchall()
        print(data)
        resp.body="hello world"
