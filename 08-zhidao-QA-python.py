import urllib.request
from urllib import request
import random
import ssl
from lxml import etree
import re
import pymysql
import json
import IPProxyPool



class zhidao(object):

    def loadPage(self, url):
        """
            作用：根据url发送请求，获取服务器响应文件
            url：需要爬去的url地址
        :return:
        """
        #请求头列表
        headers_list = [
            {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; rv,2.0.1) Gecko/20100101 Firefox/4.0.1"},
            {"User-Agent":"Mozilla/5.0 (Macintosh;Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"},
            {"User_Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"},
            {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko"},
            {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0"}
        ]

        #随机拿取请求头发送请求
        headers = random.choice(headers_list)

        #创建一个证书ssl以便访问网站
        context = ssl._create_unverified_context()
        #通过urllib进行请求发送
        requests = request.Request(url, headers = headers)
        respones = urllib.request.urlopen(requests, context = context).read().decode("gbk")

        '''测试获取页面'''
        # print(respones)

        #解析为html DOM模型
        content = etree.HTML(respones)

        # 第一种方法
        # #进行匹配，返回列表集合，取出每个帖子里面的a标签，也就是每个帖子的链接
        # xpath_a = "//div/div/div/dl/dt/a[@class="ti"]/@href"
        # #匹配列表中的time时间
        # xpath_time = "//div/div/div/dl/dd/span[@class='mr-8']/text()"
        # 调用etree的xpath语法
        # link_list = content.xpath(xpath_a)

        # 第二种方法
        # 返回所有节点的子节点
        node_list = content.xpath("//div/div/div/dl")

        #调用正则表达式提取id
        re_id = re.compile(r"\d{5,}")

        #循环过滤超链接和提问日期，提取url中id
        for link in node_list:
            links = link.xpath('./dt/a[@class="ti"]/@href')[0]
            date = link.xpath('./dd/span[@class="mr-8"]/text()')[0]
            id_list = re_id.findall(links)[0]

            items = {
                "links" : links,
                "date" : date,
                "id" : id_list
            }

            # self.write_insterData(id_list, links, date)
            #将links和id_list参数传入loadQA方法，提取超链接中的浏览数，问题，普通答案和最佳答案
            self.loadQA(items["links"], items["id"])

    def loadQA(self, link_list, id_list):
        """
            作用：取出每个链接里面的问题和答案、以及浏览次数
            link_list: 每个页面标题的超链接
            id_list: 每个url之中的id
        :return:
        """
        #请求头列表
        headers_list = [
            {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; rv,2.0.1) Gecko/20100101 Firefox/4.0.1"},
            {"User-Agent":"Mozilla/5.0 (Macintosh;Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"},
            {"User_Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"},
            {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko"},
            {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0"}
        ]
        #随机选择请求头，组合请求头
        headerTemp = random.choice(headers_list)
        headerTemp["Referer"] = "https://zhidao.baidu.com/question/" + str(id_list) + ".html"
        headers = headerTemp

        '''测试headers请求头'''
        # print(headers)

        #创建证书认证
        context = ssl._create_unverified_context()

        browes_url = "http://zhidao.baidu.com/api/qbpv?q=" + str(id_list)

        #创建request对象,获取url源码
        requestsUrl = request.Request(link_list, headers = headers)
        #创建requestsBrowse对象，获取浏览数返回
        requestsBrowse = request.Request(browes_url, headers = headers)


        #发送请求
        respones = urllib.request.urlopen(requestsUrl, context = context).read().decode("gbk")
        respones_browes = urllib.request.urlopen(requestsBrowse, context = context).read().decode("gbk")

        '''测试链接页面、测试返回浏览数'''
        # print(respones)
        # print(json.loads(respones_browes))


        content = etree.HTML(respones)

        #抓取问题,只提取第一个
        question_list = content.xpath('//div/div//h1[@accuse="qTitle"]/span/text()')
        #抓取最佳答案
        commentBest_list = content.xpath('//div/div/pre[@accuse="aContent"]/text()')
        #抓取普通答案
        commentCommon_list = content.xpath('//div/div/div[@accuse="aContent"]/span/text()')
        items = {
            "id" : json.loads((respones_browes)),
            "问题" : question_list,
            "最佳答案" : commentBest_list,
            "普通答案" : commentCommon_list
        }
        print(items)

        #接入代理中.....










        # #返回所有节点
        # node_list = content.xpath("//div/div")
        #
        # #进行提取
        # for link in node_list:
        #     #抓取问题,只提取第一个
        #     question_list = link.xpath('.//h1[@accuse="qTitle"]/span/text()')[0]
        #     #抓取最佳答案
        #     commentBest_list = link.xpath('./pre[@accuse="aContent"]/text()')[0]
        #     #抓取普通答案
        #     commentCommon_list = link.xpath('./div[@accuse="aContent"]/span/text()')[0]
        #
        #     items = {
        #         "问题" : question_list,
        #         "最佳答案" : commentBest_list,
        #         "普通答案" : commentCommon_list
        #     }
        #
        #     print(items)

    def writeinfo(self, id_list, browseNum_list, question_list, comment_best, comment_common):
        """
            作用：将获取到的浏览数，问题，普通答案，最佳答案以更新的形式存入数据库，以id为主键
        :param id_list:id列表,更新数据库语句的依据
        :param browseNum_list:每个id的浏览数获取
        :param question_list:问题列表
        :param commentBest_list:最佳答案列表
        :param commentCommon_list:普通答案列表
        :return:
        """
        pass

    def write_insterData(self, id_list, link_list, date_list):
        """
            作用：将id、链接、日期插入数据库
        :param id:url的id，作为主键存入数据库
        :param links:url链接列表
        :param date_list:百度知道问题提问时间
        :return:
        """
        # 打印测试
        # print(id_list)
        # print(links)
        # print(date_list)

        #创建connection对象,将数据库连接信息存入
        conn = pymysql.connect(host = 'localhost', port = 3306, db = 'python4', user = 'root', passwd = '123456', charset = 'utf8' )
        #通过connection对象的方法，创建cursor对象
        cursors = conn.cursor()

        #开始插入数据
        # cursors.execute("set sql_mode=''")
        cursors.execute("insert into zhidao_datas(id, link_list, date_list) VALUE ('%s', '%s', '%s')"%(id_list, link_list, date_list))
        print("数据插入成功!!!")

        #提交事件
        conn.commit()

        #关闭cursors对象
        cursors.close()

        #关闭数据库链接
        conn.close()

    def zhidaoSpider(self, begin_Page, end_Page):
        """
            作用：百度贴吧调度器，选择爬去的页数
        :param begin_Page:开始页数
        :param end_Page:结束页数
        """
        pass



if __name__ == "__main__":
    zd = zhidao()
    '''启动程序'''
    # url = "https://zhidao.baidu.com/search?word=%BB%E1%BC%C6%C5%E0%D1%B5&pn=10"
    # zd.loadPage(url)

    '''开始调用代理程序'''
    begin_num = int(input("开始(从1开始)\n\t"))
    end_num = int(input("结束\n\t"))
    zd.IPProxyPools(begin_num, end_num)
