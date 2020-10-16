"""
作者   ：bjx
创建时间   ：2020/10/16  2:11 下午 
文件名称   ：扑虎NBA爬取.PY
开发工具   ：PyCharm
"""
#分析网页
#获取网页数据
#解析数据
#爬取数据进行本地保存
import requests
import parsel #数据解析工具 （css/xpath/正则来进行解析）
from lxml import etree
import csv



def func(data):
    html = parsel.Selector(data)  # 获取解析数据的方法
    data_list = html.xpath('//tbody/tr[not (@class="color_font1 bg_a")]')
    title = html.xpath('//tbody/tr[@class="color_font1 bg_a"]')
    for data_nba in data_list:
        rank = data_nba.xpath('./td[1]/text()').get()
        name = data_nba.xpath('./td[2]/a/text()').get()
        team = data_nba.xpath('./td[3]/a/text()').get()
        score = data_nba.xpath('./td[4]/text()').get()
        hit_shot = data_nba.xpath('./td[5]/text()').get()
        h1 = data_nba.xpath('./td[6]/text()').get()
        h2 = data_nba.xpath('./td[7]/text()').get()
        h3 = data_nba.xpath('./td[8]/text()').get()
        h4 = data_nba.xpath('./td[9]/text()').get()
        h5 = data_nba.xpath('./td[10]/text()').get()
        h6 = data_nba.xpath('./td[11]/text()').get()
        h7 = data_nba.xpath('./td[12]/text()').get()
        data_dict = {
            '排名': rank, '球员': name,
            '球队': team, '得分': score, '命中-出手': hit_shot, '命中率': h1, '命中-三分': h2, '三分命中率': h3,
            '命中-罚球': h4, '罚球命中率': h5, '场次': h6, '上场时间': h7,
        }
        # 写入内容
        csv_w.writerow(data_dict)

    print(title)

for j in range(1,4):
    url = 'https://nba.hupu.com/stats/players/pts/{}'.format(j)
    response = requests.get(url)
    data = response.text
    print(j)
    if j==1:
       xp = etree.HTML(data)
       t1 = xp.xpath('//tbody/tr[@class="color_font1 bg_a"]/td/text()')  # 获取标题数据
       print(t1)
       f = open(r'/Users/baijinxing/Documents/files/nba.csv', mode='a', encoding='utf-8', newline='')  # 打开文件并写入
       csv_w = csv.DictWriter(f, fieldnames=t1)
        # 写入头部
       csv_w.writeheader()
       func(data)
    else:
        func(data)