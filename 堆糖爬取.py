"""
作者   ：bjx
创建时间   ：2020/10/14  10:09 上午 
文件名称   ：堆糖爬取.PY
开发工具   ：PyCharm
"""
#获取URL
#分析URL
#清洗数据
#保存数据到本地
import pprint#换行
import urllib.parse#进行格式转换
import requests
import json
import jsonpath#对json数据进行提取
def tuitang(name,num):
    kw = name #控制搜索内容
    k = urllib.parse.quote(kw)#将汉字转换成%E7%BE%8E%E5%A5%B3
    m = int(num/24)
    for j in range(m+1):
        n = 24 * j #控制图片数量
        url = "https://www.duitang.com/napi/blog/list/by_search/?kw={}&type={}".format(k,n)
        response = requests.get(url)
        data_m = response.text
        data_j = json.loads(data_m)
        data_list = jsonpath.jsonpath(data_j,'$..path')
        pprint.pprint(data_list)
        img_name = n
        #遍历每一个图片
        for i in data_list:
            img = requests.get(i)
            #保存数据
            path = r"/Users/baijinxing/Documents/files/img/{}{}.jpg".format(j,img_name)
            with open(path,'wb') as f:
                f.write(img.content)
                f.close()
            img_name += 1

name = input("请输入搜索内容")
num_str = input("请输入搜索图片数量")
num = int(num_str)
tuitang(name,num)
