"""
作者   ：bjx
创建时间   ：2020/11/1  8:24 下午 
文件名称   ：喜马拉雅电台.PY
开发工具   ：PyCharm
"""
import requests
#数据分析
import parsel

start_url = 'https://www.ximalaya.com/youshengshu/4256765/'
header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36'
}
response = requests.get(url=start_url,headers=header)
html = response.text
date = parsel.Selector(html)
list_li = date.xpath("//div[@class='sound-list _Qp']/ul/li")
for li in list_li:
    title = li.xpath(".//a/@title").get()
    href = li.xpath(".//a/@href").get()

    #获取ID
    id = href.split('/')[-1]

    #音频URL
    yp_url = "https://www.ximalaya.com/revision/play/v1/audio?id={}&ptype=1".format(id)
    json_d = requests.get(url=yp_url,headers = header).json()
    #获取音频对应的src
    src = json_d['data']['src']

    #二进制转换
    src_data = requests.get(url=src,headers = header).content

    with open('/Users/baijinxing/Documents/files/mp3/'+title+'.m4a',mode='wb') as f:
        f.write(src_data)
        print("保存成功")