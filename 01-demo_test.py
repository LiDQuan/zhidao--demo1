
import urllib.request
from bs4 import BeautifulSoup
#import requests
from lxml import etree
import ssl
from urllib import request



def zhihuLogin():
    # Page = 50


    # 放入url和请求头，并且发送open信息
    url = "https://tieba.baidu.com/f?kw=%E4%BC%9A%E8%AE%A1&pn=50/"
    # url_o = "http://www.baidu.com/"

    new_header = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"
    }

    context = ssl._create_unverified_context()


    re = request.Request(url)
    op_re = urllib.request.urlopen(re, context = context).read().decode('utf8')
    # op_re.encoding = 'utf-8'
    # print(op_re)

    xxxml = etree.HTML(op_re)
    # link_list = xxxml.xpath('//div/div/a/@class')
    link_list = xxxml.xpath('//div[@class="t_con cleafix"]/div/div/div/a/@title')
    for link in link_list:
        print (link)







    #方法二 使用requests发送请求，同时构建一个session对象，可以保存页面的cookie值




    # print(op_re.read().decode("utf-8"))

    #开始使用beautifulSoup,指定bs4解析器为"html.parser"
    # soup = BeautifulSoup(op_re.read(), 'html.parser')

    # some = soup.find_all('div')
    #
    # for ai in some:
    #     print( ai )




    # print( soup.prettify())



    #urlretrieve()方法是request中的下载函数，调用该函数，完成下载的目的
    #down = urllib.request.urlretrieve()



    #显示soup类型
    # print(type(soup))

    # prettify()格式化输出 soup 对象内容
    # print( soup.prettify() )

    #显示soup中的tittle标签
    # print(soup.title)


    #搜索文档 find_all() find get_text()
    #print( soup.get_text() )

    #find_all 的参数 字符串 正则 方法 list
    #find_all 返回的是一个列表
    # a = soup.find_all('div')
    #print( a )
    # for b in a:
    #     link = b
    #     print(link)

    #find查找，用法,find(标签，属性)
    #class后面添加的"_",是python的关键词，所以要放置下划线
    # print( soup.find('div',class_="wrap2") )



zhihuLogin()