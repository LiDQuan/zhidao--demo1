import urllib.request
import ssl
from lxml import etree




class IPProxyPools_new(object):
    def IPProxyPools(self, begin_num, end_num):
        """
            作用：调度器，决定爬取的代理页数
            begin_num:开始页数
            end_num:结束页数
        :return:
        """
        headers = {
            "User-Agent": "Mozilla/5.0(Macintosh;IntelMacOSX10_7_0)AppleWebKit/535.11(KHTML,likeGecko)Chrome/17.0.963.56Safari/535.11"
        }
        context = ssl._create_unverified_context()
        # 爬取爬虫网站，爬取代理ip
        for num in range(begin_num, end_num + 1):
            url_kuaidaili = "https://www.kuaidaili.com/free/inha/" + str(num)
            requests = urllib.request.Request(url_kuaidaili, headers=headers)
            respones = urllib.request.urlopen(requests, context=context).read().decode("utf-8")
            self.down_IPProxyPools(respones)
            #
            #     print(items)

    def down_IPProxyPools(self, url_list):
        """
            作用：抓取代理并下载存入数据库
            url：需要抓取的代理网页
        :return:
        """
        # 转化成HTML DOM
        html = etree.HTML(url_list)
        # 创建根节点
        IpList = html.xpath("//table//td[@data-title='IP']/text()")
        PortList = html.xpath("//table//td[@data-title='PORT']/text()")
        #拆包
        for ip,prot in zip(IpList,PortList):
            # print (ip,prot)
            self.check_IP(ip, prot)
            # items = {
            #     "ip":IpList,
            #     "port":PortList
            # }
            # print(items)
            # 将获取的代理进行访问验证，访问某个网站
            # 如果成功则返回连接代码，则存入IPpool_list，并且直接传入主程序爬虫
            # 构建一个Handler处理器对象，参数是一个字典,python3中要调用urllib
            # httpproxy_handler = urllib.request.ProxyHandler(IPpool_list)
    def check_IP(self, ip_list, port_list):
        """
            作用：测试代理ip地址
            IP_list:ip列表
            port_list:端口号
        :return:
        """
        # 组合代理
        print()
        # print("%s,%s"%(ip_list,port_list))

if __name__ == "__main__":
    new = IPProxyPools_new()
    begin_num = int(input("开始(从1开始)\n\t"))
    end_num = int(input("结束\n\t"))
    new.IPProxyPools(begin_num, end_num)