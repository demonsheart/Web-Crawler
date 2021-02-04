# 如何构造http请求, 如获取 https://api.cosmostation.io/v1/status 的 total_circulating_tokens 字段属性（php,python）

import requests
import json

r = requests.get('https://api.cosmostation.io/v1/status')

st = r.text  # 返回文本
dic = json.loads(st)  # 转换为dict
re = dic['total_circulating_tokens']
print(re)
