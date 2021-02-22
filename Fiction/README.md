### scrapy 实战

* 需求

  > 从[笔趣阁](https://www.biquge5200.com/)上爬取一本完整的小说

* 思路

  > 从第一章节开始，xpath爬取正文，通过网页上的“下一页”中获取URL，一章一章的爬取
  >
  > 启用pipelines写入文件
  >
  > 由于页面有反爬，开启DOWNLOADER_MIDDLEWARES，设置User_Agent代理池，并且设置DOWNLOAD_DELAY，仍旧有一定的失败几率（scrapy默认重试三次），通过重新设定重试次数为10，成功爬取

* 运行
  > biquge5200.py的start_urls下填入笔趣阁网址下想要下载的小说的第一章的URL，然后命令行启动：

  ```cmd
  scrapy crawl biquge5200
  ```

* PS
  > 由于爬下来的小说比较大，不上爬取结果文件
  > 不排除失败的可能，可以适当上调延迟DOWNLOAD_DELAY以及增加重试次数RETRY_TIMES
  > 由于未设置ip代理池，也有被封ip的风险，仅供学习使用。