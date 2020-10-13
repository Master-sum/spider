"""
作者   ：bjx
创建时间   ：2020/10/13  10:37 下午 
文件名称   ：雪球.PY
开发工具   ：PyCharm
"""
import pprint
import csv
import requests
def sueqiu():
    file = open('/Users/baijinxing/Documents/files/data.csv',mode='a',encoding='utf-8',newline='')#打开文件
    csv_header = csv.DictWriter(file,fieldnames=['股票名称','当前股价'])
    csv_header.writeheader()#写入表头
    for i in range(1,30):
        URL="https://xueqiu.com/service/v5/stock/screener/quote/list?page=%d&size=30&order=desc&order_by=percent&exchange=CN&market=CN&type=cyb&_=1602599985550"%i
        header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}
        response = requests.get(url=URL,headers=header)
        data = response.json()
        data_list = data['data']['list']
        for i in data_list:
            name = i['name']
            current = i['current']
            print(name,current)
            # pprint.pprint(i)
            #本地化
            data_dict = {'股票名称':name,'当前股价':current}
            csv_header.writerow(data_dict)#循环写入内容

if __name__ == "__main__":
    sueqiu()