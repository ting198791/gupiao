from .sql import Sql
from twisted.internet.threads import deferToThread
from gupiao.items import GupiaoItem


class gupiaoPipeline(object):

    def process_item(self, item, spider):
        #deferToThread(self._process_item, item, spider)
        if isinstance(item, GupiaoItem):
          code = item['code']
          name = item['name']
          market = item['market']

          Sql.insert_gupiao(self,code,name,market)
          print('插入数据')
          return item

