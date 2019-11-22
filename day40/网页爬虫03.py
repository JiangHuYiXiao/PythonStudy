# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/11/22 16:54
# @Software       : Python_study
# @Python_verison : 3.7
# 爬取十个网页的任务
from gevent import monkey;monkey.patch_all()            # 添加在首行为了是可以识别IO,time的，网络延迟的等
from threading import Thread
import requests
import gevent
import time
def get_url(url):
    res = requests.get(url)         # 这个地方会有时间等待IO
    print((url,res.status_code,res.text))
url_list = [
    'http://www.baidu.com',
    'http://www.qq.com',
    'http://www.python.org',
    'http://www.mi.com',
    'http://www.cnblogs.com',
    'http://www.sohu.com',
    'http://www.apache.org',
    'http://www.taobao.com',
    'http://www.360.com'
]

g_lst = []
start_time = time.time()
for url in url_list:
    get_url(url)
print(time.time()-start_time)


for url in url_list:
    g = gevent.spawn(get_url,url)           # 创建协程对象，并且传参数
    g_lst.append(g)
gevent.joinall(g_lst)
print(time.time()-start_time)
# 协程更快


