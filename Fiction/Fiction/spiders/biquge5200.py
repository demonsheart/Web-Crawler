import scrapy
from Fiction.items import FictionItem


class Biquge5200Spider(scrapy.Spider):
    name = 'biquge5200'
    allowed_domains = ['biquge5200.com']
    start_urls = ['https://www.biquge5200.com/76_76490/147016121.html']

    def parse(self, response):
        title = response.xpath(
            '//div[@class="bookname"]/h1/text()').extract()[0]
        lines = response.xpath('//div[@id="content"]/p/text()').extract()
        content = ''
        for line in lines:
            content = content + line + '\n\n'

        item = FictionItem()
        item['title'] = title
        item['content'] = content

        yield item

        next_url = response.xpath(
            '//div[@class="bottem2"]/a[4]/@href').extract_first()
        if next_url.find('.html') != -1:
            yield scrapy.Request(next_url, callback=self.parse)
