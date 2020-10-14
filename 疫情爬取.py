"""
作者   ：bjx
创建时间   ：2020/10/14  11:04 上午 
文件名称   ：疫情爬取.PY
开发工具   ：PyCharm
"""
import pprint
import time,requests
import json
url = "https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5&callback=&_=%d"%int(time.time()*1000)
response = requests.get(url)
data = json.loads(response.json()['data'])
china_city = data['areaTree'][0]['children']
data_city_total = []
#遍历list中每一个城市
for i in china_city:
    data_list = {}
    data_list['城市'] = i['name']
    data_list['今日确诊'] = i['today']['confirm']
    data_list['现有确诊'] = i['total']['nowConfirm']
    data_list['累计确诊'] = i['total']['confirm']
    data_list['治愈'] = i['total']['heal']
    data_list['死亡'] = i['total']['dead']
    data_city_total.append(data_list)
pprint.pprint(data_city_total)