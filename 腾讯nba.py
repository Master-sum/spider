"""
作者   ：bjx
创建时间   ：2020/10/16  5:03 下午 
文件名称   ：腾讯nba.PY
开发工具   ：PyCharm
URL='https://ziliaoku.sports.qq.com/cube/index?cubeId=10&dimId=52&from=sportsdatabase&order=t70&params=t2:2014|t3:2|&limit=0,50'
"""
import pprint

import requests
import csv

f = open(r'/Users/baijinxing/Documents/files/nba.csv',mode='a',encoding='utf-8',newline='')
csv_writer = csv.DictWriter(f,fieldnames=['球员','得分','时间'])
csv_writer.writeheader()
for j in range(2014,2020):
    URL='https://ziliaoku.sports.qq.com/cube/index?cubeId=10&dimId=52&from=sportsdatabase&order=t70&params=t2:{}|t3:2|&limit=0,50'.format(j)
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}
    response = requests.get(url=URL, headers=header)
    data = response.json()
    data_list = data['data']['nbaPlayerSeasonStatRank']

    pprint.pprint(data_list)
    for i in range(50):
        name = data_list[i]['cnName']
        teamName = data_list[i]['teamName']
        pointsPG = data_list[i]['pointsPG']
        minutesPG = data_list[i]['minutesPG']
        print(name,teamName,pointsPG,minutesPG)
        data_dict = {
            '球员':name,'得分':pointsPG,'时间':j
        }
        csv_writer.writerow(data_dict)
f.close()