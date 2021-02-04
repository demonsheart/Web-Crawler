### scrapy案例

* 要求
> 1. 爬取[腾讯招聘](https://careers.tencent.com/search.html)网页下所有招聘信息
> 2. 以jsonlines格式存进data文件夹

* 思路
> 由于是动态网页，直接爬取页面甚至连数据标签都找不到
> 利用XHR爬取
> 先通过一次单页面请求到总记录数，然后计算生成所有页面下的url，再进行爬取

* 运行
```cmd
cd data
scrapy crawl tencent
```

* PS
> 事实上用单个py文件处理即可 用框架主要是为了熟悉
