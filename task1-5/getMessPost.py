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
    'token': '',
    'lang': 'zh',
    'BZ-SessionId': 'DJ4vmDC3CR_N0_0Ekt1fhEE0e2bVQ5Ut62A3paq9QOE665HUcHu2ZwnB6vkL8ZECTURnuTl3iFyyofbqy0z2UA',
    'sa_origin_id': '17743e9dd831a3-02e854c5a7642c-c791039-1327104-17743e9dd84683',
    'nonce': '890958',
    '_CDID': '100002',
    '_CDCODE': '57161dff581b045e8cf893e233c44a33'
}
forms = []
for n in range(1, 12):
    form['current_page'] = n
    forms.append(dict(form))

for dat in forms:
    r = session.post(url, data=dat)
    r.encoding = 'utf-8'
    js = r.json()
    with open('getMess_post.txt', 'ab') as fd:
        for x in js['data']['list']:
            x_url = 'https://help.bitz.ai/article/' + str(x['id'])
            x_title = x['title_zh']
            print(x_title, x_url)
            fd.write((x_title + ' ' + x_url + '\n').encode(encoding='utf-8'))

