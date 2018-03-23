#负责发送请求
from urllib import request
import urllib
import ssl
# json解析库，对应到lxml
import json
# json的解析语法，对应到xpath
import jsonpath



url = "https://www.lagou.com/lbs/getAllCitySearchLabels.json"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36"}

# 多了一个创建证书ssl的步骤，当目标网站使用的是自签名的证书的时候，会抛出一个urllib:URLerror的消息错误，接下来，需要import ssl，创建未经验证的上下文，在urlopen中传入上下文参数
context = ssl._create_unverified_context()

#发送请求，返回一个request对象
requests = request.Request(url, headers = headers)
response = urllib.request.urlopen(requests, context = context)

#取出json文件中的字符串内容
html = response.read().decode('utf-8')

#把json文件转化为python形式的unicode字符串
unicoder = json.loads(html)

#调用jsonpath的方法，过滤出想要的数据
#过滤出所有的城市名，匹配成功返回一个字符串列表
#python形式的列表
str_list = jsonpath.jsonpath(unicoder, "$..name")

#测试
#for temp in str_list:
#   print(temp)


#









#打印测试
#print(response.read().decode('utf-8'))

