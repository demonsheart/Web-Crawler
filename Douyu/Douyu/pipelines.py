# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# useful for handling different item types with a single interface

# 1、导入
# from scrapy.utils.project import get_project_settings
# 2、在需要的地方
#  settings = get_project_settings()
# 3、通过settings[name]进行获取
# 例如：
# settings["MYSQL_HOST"]
import scrapy
import os
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy.utils.project import get_project_settings


class DouyuPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        for file_url in item['imagelink']:
            yield scrapy.Request(file_url)

    def item_completed(self, results, item, info):
        file_paths = [x['path'] for ok, x in results if ok]
        if not file_paths:
            raise DropItem("Item contains no files")
        settings = get_project_settings()
        images_store = settings['IMAGES_STORE']
        os.rename(images_store + file_paths[0], images_store + item['nickname'] + '.jpg')

        return item
