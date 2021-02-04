# 爬取公告列表https://help.bitz.ai/section/100000019 (分析页面，构造http请求)
# post

import requests

proxies = {
    "http": "socks5://127.0.0.1:10808",
    "https": "socks5://127.0.0.1:10808",
}

session = requests.Session()

session.proxies.update(proxies)

url = 'https://help.bitz.ai/article/list'

form = {
    'page_size': '10',
    'current_page': '1',
    'section_id': '100000019',
    'channel': 'web',
    'lang': 'zh',
}
forms = []
for n in range(1, 12):
    form['current_page'] = n
    forms.append(dict(form))

with open('getMessPost.txt', 'wb') as fd:
    for dat in forms:
        r = session.post(url, data=dat)
        r.encoding = 'utf-8'
        js = r.json()
        for x in js['data']['list']:
            x_url = 'https://help.bitz.ai/article/' + str(x['id'])
            x_title = x['title_zh']
            print(x_title, x_url)
            fd.write((x_title + ' ' + x_url + '\n').encode(encoding='utf-8'))

