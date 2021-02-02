import scrapy
from ITcast.items import ItcastItem


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['www.itcast.cn']
    start_urls = ['http://www.itcast.cn//channel/teacher.shtml']

    def parse(self, response):
        node_list = response.xpath(
            "//ul[@class='clears']/li/div[@class='main_mask']")
        
        # items = []
        
        for node in node_list:
            item = ItcastItem()
            # .extract() 将xpath对象转化为字符串
            item['name']  = node.xpath("./h2/text()").extract()[0]
            item['time'] = node.xpath("./h3/text()").extract()[0]
            item['info'] = node.xpath("./p/text()").extract()[0]

            # items.append(item)

            # 每次循环返回item类型 自动识别进入pipeline
            yield item

        # 直接返回，不经过pipeline 可经过命令导出为json, csv等文件
        # return items
