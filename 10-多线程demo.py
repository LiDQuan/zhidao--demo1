#创建队列的库
import queue
#解析库
from lxml import etree
#请求处理
import requests
#json处理
import json
#创建线程的类
import threading

class ThreadCrawl(threading.Thread):
    def __int__(self, threadName, pageQueue, dataqueue):
        #调用父类初始化方法
        super(ThreadCrawl, self).__init__()
        #线程名
        self.threadName = threadName
        #页码队列
        self.pageQueue = pageQueue
        #数据队列
        self.dataqueue = dataqueue

    def run(self):
        while True:
            try:
            #取出一个数字，先进先出
            #可选参数block，默认值为True
            #1、如果队列为空，block为True的话，就会进入阻塞状态，直到队列有新的数据
            #2、如果队列为空，block为False的话，就会弹出一个Queue.empty(),异常
                page = self.pageQueue.get(False)
            except:
                pass


def main():
    # 页码的队列，表示可以存储10个页面
    pageQueue = queue(10)

    # 放入了1~10的数字，先进先出
    for i in pageQueue(1,11):
        pageQueue.put(i)


    #采集结果(每页的HTML源码)的数据队列，参数为空表示不限制
    dataqueue = queue()

    #开始线程创建
    # 存储三个采集线程的名字
    crawList = ["一号", "二号", "三号" ]

    # 存储三个采集线程
    threadcrawl = []
    for threadName in crawList:
        thread = ThreadCrawl(threadName, pageQueue, dataqueue)
        thread.start()
        threadcrawl.append(thread)


