"""
作者   ：bjx
创建时间   ：2020/10/11  9:03 下午 
文件名称   ：tiobe_python.PY
开发工具   ：PyCharm
"""
#爬取编程排行
import csv
import requests,re
class Tiobe_python(object):
    def __init__(self):
        self.url = "https://www.tiobe.com/tiobe-index"
        self.headers = {
        'User-Agent': 'Mozilla/5.0(Macintosh;IntelMac OS X 10_15_6) AppleWebKit/537.36(KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
        }
        #保存位置
        self.table = '/Users/baijinxing/Documents/spider/files/tiobe.csv'

    #爬虫文件
    def spider_file(self):
        print("开始执行")
        #发送请求
        text = requests.get(self.url,headers = self.headers).text
        print(text)
        #获取全部内容
        content = ''.join(re.findall(r'series: (.*?)\}\);',text,re.DOTALL))
        print(content)
        #获取编程语言
        series = re.findall(r'({.*?})',content,re.DOTALL)
        print(series)
        #将内容写入
        with open(self.table,'w',newline='') as f:
            self.writer = csv.DictWriter(f,['name','value','date'])
            self.writer.writeheader()

            for content_spider in series:
                name = ''.join(re.findall(r"{name : '(.*?)'", content_spider, re.DOTALL))

                date = re.findall(r"\[Date.UTC(.*?)\]", content_spider, re.DOTALL)
                for i in date:
                    i = i.replace(' ', '')
                    i = re.sub(r'[()]', '', i)
                    value = i.split(',')[-1]
                    date_list = i.split(',')[:3]
                    time = ""
                    for index, j in enumerate(date_list):
                        if index != 0:
                            if len(j) == 1:
                                j = '0' + j

                        if index == 0:
                            time += j
                        else:
                            time += '_' + j
                    i_dict = {
                        'name': name,
                        'value': value,
                        'date': time

                    }
                    print(i_dict)
                    self.writer.writerow(i_dict)

if __name__ == "__main__":
    t = Tiobe_python()
    t.spider_file()
