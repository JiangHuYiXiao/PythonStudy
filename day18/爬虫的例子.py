# -*- coding:utf-8 -*-
# 需求：爬取豆瓣电影top250的电影名字，评分，多少人评价获取到指定的文件中
from urllib.request import urlopen
import json
import re

# 首先，获取豆瓣电影的源码
def getpage(url):
    response = urlopen(url)
    return response.read().decode('utf-8')  # 爬虫获取到的html都是bytes类型，编码方式为gbk，解码成utf-8

# 其次，分析获取到的网页源码，通过正则表达式获取到我们需要的信息（名字、评分、评价）
def parsepage(s):
    com = re.findall(
        '<div class="item">.*?<div class="pic">.*?<em.*?>(?P<id>\d).*?<span class="title">(?P<title>.*?)</span>'
        '.*?<span class="rating_num" property="v:average">(?P<rating_num>.*?)</span>.*?<span>(?P<comment_num>.*?)</span>',s,re.S)
        # ？P<名字>给分组起一个名字，以后可以通过名字去找
    return com

def main(num):
    url = 'https://movie.douban.com/top250?start=%s&filter=' % num
    response_html = getpage(url)
    ret = parsepage(response_html)
    print(ret)
    f = open('move_info',mode='a',encoding='utf-8')
    for object in ret:
        print(object)
        data= str(object)
        f.write(data+'\n')


count = 0
for i in range(10):
    main(count)
    count += 25

