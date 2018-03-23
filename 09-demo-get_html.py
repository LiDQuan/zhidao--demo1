from urllib import request
import urllib.request
import lxml.html
from lxml import etree
import ssl
import json
import queue


url2 = "http://zhidao.baidu.com/api/qbpv?q=2116306482279866467"

headers = {
        "User_Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
        # "Cookie": "BAIDUID=571263451459A1961526EDA4BF778881:FG=1; BIDUPSID=571263451459A1961526EDA4BF778881; PSTM=1520581348; pgv_pvi=5270509568; H_PS_PSSID=1422_25548_21116_18560_17001_20927; PSINO=7; Hm_lvt_6859ce5aaf00fb00387e6434e4fcc925=1521162387; Hm_lvt_0bd5902d44e80b78cb1cd01ca0e85f4a=1521162387; Hm_lpvt_6859ce5aaf00fb00387e6434e4fcc925=1521425177; Hm_lpvt_0bd5902d44e80b78cb1cd01ca0e85f4a=1521428252; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598",
        "Referer":  "https://zhidao.baidu.com/question/982123176821278299.html"
}

values= {
}

# context = ssl._create_unverified_context()

data = urllib.parse.urlencode(values).encode('utf-8')
requests = request.Request(url2 ,data = data ,headers = headers)
respones = urllib.request.urlopen(requests).read().decode("gbk")

# html = respones.read().decode("gbk")
# print(html)

print(json.loads(respones))

