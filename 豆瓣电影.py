"""
作者   ：bjx
创建时间   ：2020/11/20  11:12 下午 
文件名称   ：豆瓣电影.PY
开发工具   ：PyCharm
坚持：山穷水复疑无路，柳暗花明又一村
"""
import requests
import time
import random
from queue import Queue
from lxml import etree
class DouBanSpider:
    #初始化
    def __init__(self):
        #初始化头部
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36'
        }
        #初始化URL
        self.url = "https://movie.douban.com/top250"
        #初始化队列
        self.dataQ = Queue()
        #编号
        self.num = 1
    #请求获取界面
    def loadPage(self,url):
        #随机休眠
        time.sleep(random.random())
        #请求网页
        return requests.get(url,headers = self.header).content
    #解析页面内容
    def parsePage(self,url):
        #获取界面
        content = self.loadPage(url)
        #xpath解析
        html = etree.HTML(content)
        node_list = html.xpath("//div[@class='info']")
        for node in node_list:
            title = node.xpath(".//span[@class='title']/text()")[0]
            score = node.xpath(".//span[@class='rating_num']/text()")[0]
            #将内容如队列
            self.dataQ.put(score+"\t"+title)
        #当第一页获取全部界面连接
        if url == self.url:
            return [self.url+link for link in html.xpath("//div[@class='paginator']/a/@href")]
    #遍历下一页
    def starW(self):

        link_list = self.parsePage(self.url)
        for link in link_list:
            self.parsePage(link)
        #判断队列是否为空
        while not self.dataQ.empty():
            print(self.num)
            print(self.dataQ.get())
            self.num += 1

if __name__ == "__main__":
    #创建爬虫对象
    spider = DouBanSpider()

    start = time.time()
    #开始爬虫
    spider.starW()

    stop = time.time()
    endtime = stop-start
    print(endtime)
