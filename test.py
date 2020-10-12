"""
作者   ：bjx
创建时间   ：2020/10/11  10:27 下午 
文件名称   ：test.PY
开发工具   ：PyCharm
'cookie': '_ga = GA1.2.1894941539.1602408831;gid = GA1.2.1304870113.1602408831;_gads = ID = 24f863db3fad7bbe: T = 1602408835:S = ALNI_MaPxd1jnh5jhPyGOn_NSMOmV4csQ',
        'sec - ch - ua': '"\\Not;A\"Brand";v = "99", "Google Chrome";v = "85", "Chromium";v = "85"',
        'sec - ch - ua - mobile': '?0',
        'sec - fetch - dest': 'document',
        'sec - fetch - mode': 'navigate',
        'sec - fetch - site': 'none',
        'sec - fetch - user': '?1',
"""
from http.cookiejar import CookieJar

import requests
def re_t():
    url = "https://www.tiobe.com/tiobe-index"
    cookie = CookieJar()
    print(cookie)
    headers = {
        # 'Referer': 'https://www.tiobe.com/',
        # 'cookie':'{}'.format(cookie),
        'User-Agent': 'Mozilla/5.0(Macintosh;IntelMac OS X 10_15_6) AppleWebKit/537.36(KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',


    }
    text = requests.get(url=url,headers=headers)
    print(text)

re_t()