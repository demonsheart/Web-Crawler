# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json


class ItcastPipeline:
    def __init__(self):
        self.f = open("itcast_pipeline.json", 'wb')
        self.f.write('[\n'.encode("utf-8"))

    def process_item(self, item, spider):
        content = json.dumps(dict(item), ensure_ascii=False) + ',\n'
        self.f.write(content.encode("utf-8"))
        return item  # 不可缺 返回信号

    def close_spider(self, spider):
        self.f.write(']'.encode("utf-8"))
        self.f.close()
