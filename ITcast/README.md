### scrapy案例

* 要求
> 1. 爬取[itcast](http://www.itcast.cn//channel/teacher.shtml)网页下所有老师信息
> 2. 存进data文件夹

* 思路
> 由于是静态网页 直接爬取页面 用scrapy自带的xpath选择数据，历经pipelines处理即可
