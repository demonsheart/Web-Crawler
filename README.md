### 爬虫学习

1. 搭建python环境
2. 了解python语法
3. 什么是爬虫？爬虫的应用？
4. 如何构造http请求, 如获取 https://api.cosmostation.io/v1/status 的 total_circulating_tokens 字段属性（php,python）
> easySpider.py
5. 如何请求网页 https://www.binance.com/cn/support/announcement/aec178a59f824162ab77a17a5d0838a5, 提取网页信息（如正则表达式，css选择器, xpath）
> getMessage.py
6. 爬取公告列表 https://www.binance.com/cn/support/announcement/c-48, https://help.bitz.ai/section/100000019 (分析页面，构造http请求)
> (1) 爬取第一个链接： 
> getTitle.py getTitleURL.py getAllMes.py
> 爬取标题+时间+内容耗时较长 且只能爬取公告内容在article标签的页面（爬到标题为 “币安合约将上线ETHUSD次季1225交割合约”）

> (2) 爬取第二个链接: 
> getMessPost.py
7. 了解学习scrapy框架

备注：
* 梯子自备
* 安排5中，提取公告的标题、内容、时间
* 安排6中，需要爬取所有页数下的公告标题