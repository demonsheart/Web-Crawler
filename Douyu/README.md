### scrapy案例

* 要求
> 1. 爬取[Douyu](http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset=1)直播间接口下的图片
> 2. 存进 settings.py 下的 IMAGES_STORE指定的文件夹

* 思路
> json获取链接直接下载即可

* 运行
```cmd
scrapy crawl douyu
```
