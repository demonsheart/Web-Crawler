# 如何请求网页 https://www.binance.com/cn/support/announcement/aec178a59f824162ab77a17a5d0838a5, 提取公告的标题、内容、时间
# css选择器

import requests
import re
from bs4 import BeautifulSoup

proxies = {
    "http": "socks5://127.0.0.1:10808",
    "https": "socks5://127.0.0.1:10808",
}

session = requests.Session()
session.proxies.update(proxies)

url = 'https://www.binance.com/cn/support/announcement/aec178a59f824162ab77a17a5d0838a5'

web_data = session.get(url)

web_text = web_data.text

soup = BeautifulSoup(web_text, features="html.parser")

title = (soup.select('.css-1ezl0c')[0]).text

time = (soup.select('.css-f1q2g4')[0]).text

art = (soup.select('article')[0]).text

article = re.match(r'.*[0-9]{4}年[0-9]{1,2}月[0-9]{1,2}日', art)

result = {'title': title, 'time': time, 'article': article.group()}

print(result)