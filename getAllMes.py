# 如何请求网页 https://www.binance.com/cn/support/announcement/c-48, 提取网页信息（如正则表达式，css选择器, xpath）
# 提取title + URL + time + article 写入message.txt

import requests
import re
from bs4 import BeautifulSoup


def getArt(URL):
    text = session.get(URL).text
    soup = BeautifulSoup(text, features="html.parser")
    art = (soup.select('article')[0]).text
    time = (soup.select('.css-f1q2g4')[0]).text
    article = re.match(r'.*[0-9]{4}年[0-9]{1,2}月[0-9]{1,2}日', art)
    return article.group(), time


proxies = {
    "http": "socks5://127.0.0.1:10808",
    "https": "socks5://127.0.0.1:10808",
}

session = requests.Session()

session.proxies.update(proxies)

urls = [
    'https://www.binance.com/gateway-api/v1/public/cms/article/catalog/list/query?catalogId=48&pageNo={}&pageSize=15'.format(
        str(i)) for i in range(1, 44)]

headers = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'content-type': 'application/json',
    'cookie':
        '_ga=GA1.2.1159601895.1611395450; bnc-uuid=432bf6ed-1d55-48bc-bede-9cfba8d839a5; userPreferredCurrency=USD_USD; _gid=GA1.2.1886009461.1611644862; source=referral; campaign=www.binance.com; BNC_FV_KEY=311ae6c135e0ab928b45fd52dac72305bca75e1b; BNC_FV_KEY_EXPIRE=1611821195280',
    'csrftoken': 'd41d8cd98f00b204e9800998ecf8427e',
    'lang': 'cn',
    'referer': 'https://www.binance.com/cn/support/announcement/c-48',
    'user-agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}

preURL = 'https://www.binance.com/cn/support/announcement/'
for url in urls:
    r = session.get(url, headers=headers)
    r.encoding = 'utf-8'
    js = r.json()
    with open('message.txt', 'ab') as fd:
        for x in js['data']['articles']:
            artURL = preURL + x['code']
            fd.write((x['title'] + '    ' + artURL + '\n').encode(encoding='utf-8'))
            art, time = getArt(artURL)
            fd.write((time + '\n' + art + '\n\n').encode(encoding='utf-8'))

