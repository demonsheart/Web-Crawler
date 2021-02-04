import scrapy
import math
import requests
from Tencent.items import TencentItem
from urllib.parse import urlencode


class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['careers.tencent.com']
    start_urls = ['https://careers.tencent.com/tencentcareer/api/post/Query?']

    def start_requests(self):
        # 请求一次获得记录数 然后计算出页面数
        data = {
            'pageIndex': '1',
            'pageSize': '10',
            'language': 'zh-cn',
            'area': 'cn'
        }
        param = urlencode(data)
        url = self.start_urls[0] + param
        tmpRe = requests.get(url)
        count = tmpRe.json()['Data']['Count']
        page = math.ceil(count / 10)

        # 生成url
        urls = []
        for i in range(1, page + 1):
            data['pageIndex'] = str(i)
            param = urlencode(data)
            url = self.start_urls[0] + param
            urls.append(str(url))
        
        # 回调parse
        for url in urls:
            yield scrapy.Request(url, dont_filter=True, callback=self.parse)

    def parse(self, response):
        js = response.json()['Data']['Posts']
        item = TencentItem()
        for x in js:
            item['BGName'] = x['BGName']
            item['CategoryName'] = x['CategoryName']
            item['CountryName'] = x['CountryName']
            item['LastUpdateTime'] = x['LastUpdateTime']
            item['LocationName'] = x['LocationName']
            item['URL'] = x['PostURL']
            item['ProductName'] = x['ProductName']
            item['RecruitPostId'] = x['RecruitPostId']
            item['RecruitPostName'] = x['RecruitPostName']
            item['Responsibility'] = x['Responsibility']
            # 交给pipelines处理
            yield item

