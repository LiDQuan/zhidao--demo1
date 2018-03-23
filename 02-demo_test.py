#!/usr/bin/env python
# -*- coding:utf-8 -*-



# 使用模拟登陆进行知乎登陆
# from bs4 import BeautifulSoup
import requests
from bs4 import BeautifulSoup


def zhihudenglu():
    #构建一个session对象，可以保存cookie
    sess = requests.Session()


    #编辑请求头
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36"}

    #首先获取登录页面，找到需要post的数据  ，同时会记录当前页面的cookie值
    html = sess.get("http://www.zhihu.com/#signin",headers = headers).text
    #调用lxml解析库
    bs = BeautifulSoup(html,"lxml")

    #测试获取的html页面是否正常
    # print(bs)

    #获取之前get的页面里的_xsrf值，但是最新版本的知乎登录已经取消了_xsrf值得设定
    _xsrf = bs.find("img",attrs={"class":"Captcha-englishImg"}).get("data-tooltip")
    # _xsrf = bs.find("input", attrs={"name":"_xsrf"})
    print (_xsrf)

zhihudenglu()