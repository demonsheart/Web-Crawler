## scrapy开发步骤
[other's note](https://blog.csdn.net/fallwind_of_july/article/details/97246577)
1. scrapy startproject XXXX
2. cd XXXX
3. scrapy genspider XXX XXX
4. 编写 items.py ，明确需要提取的数据
5. 编写 spiders/xxx.py 编写爬虫文件，处理请求和响应，以及提取数据(yeild item)
6. 编写 pipelines,py 编写管道文件，处理spider返回item数据
7. 编写settings.py 启动管道组件，以及其他相关设置
8. 执行爬虫