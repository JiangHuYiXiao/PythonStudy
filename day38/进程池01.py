# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/11/14 8:35
# @Software       : Python_study
# @Python_verison : 3.7
# 进程池出现的原因：
# 1、创建、启动多进程太耗时间
# 2、进程太多，操作系统的调度效率也会很慢
# 所以会有进程池的出现，开进程池会有现成的进程在池子里面。
# 有任务来了就可以直接用池子中的进程去处理任务，处理完成后，再把进程放回池子里面。
# 池子中的进程就去处理其他任务了，当所有的任务都处理完成后，进程池关闭，回收所有的进程。
# 进程池开的数量一般为：内核数+1，最多是内核数*2.5
# 进程池，都是可以有返回值的

'''
# 1、进程池同步调用（顺序执行）
from multiprocessing import Pool
import time
def func(i):
    time.sleep(1)
    i+=1
    print(i)

if __name__ == '__main__':
    po = Pool(5)            # 本机内核为4
    for i in range(10):
        po.apply(func,args=(i,))


# 2、进程池异步调用（非顺序执行、并发执行）
from multiprocessing import Pool
import time
def func(i):
    time.sleep(1)
    i+=1
    print(i)            # 这样输出的结果为并发5个一起输出

if __name__ == '__main__':
    po = Pool(5)            # 本机内核为4
    for i in range(10):
        po.apply_async(func,args=(i,))              # 异步，阻塞，和主进程都是异步的，执行到这里时主进程代码结束，子进程打印的数据没有展示出来，但是进程池中的进程还没有关闭，浪费内存
    po.close()
    po.join()               # 所以添加join等待子进程的结束          #ValueError: Pool is still running，所以需要在join之前先close pool

# 3、进程池同步调用，且有返回值
from multiprocessing import Pool
import time
def func(i):
    time.sleep(1)
    i += 1
    # print(i)
    return i
if __name__ == '__main__':
    po = Pool()
    for i in range(10):
        print(po.apply(func,args=(i,)))


# 4、进程池异步调用，且有返回值
from multiprocessing import Pool
import time
def func(i):
    time.sleep(1)
    i += 1
    # print(i)
    return i
if __name__ == '__main__':
    po = Pool()
    for i in range(10):
        print(po.apply_async(func,args=(i,)).get())         # 这样输出的结果又是同步顺序输出1,2,3....


# 修改
from multiprocessing import Pool
import time
def func(i):
    time.sleep(1)
    i += 1
    return i
if __name__ == '__main__':
    po = Pool()
    l = []
    for i in range(10):
        res = po.apply_async(func,args=(i,))        #
        l.append(res)
    po.close()              # 循环外
    po.join()               # 循环外
    [print(i.get()) for i in l]         #  这样输出的结果才是真的异步并发输出1到10


# 5、map(func,iter) 第二个位置参数必须可迭代的
from multiprocessing import Pool
import time
def func(i):
    i += 1
    # print(i)            # return也可以
    return i
if __name__ == '__main__':
    po = Pool()
    res = po.map(func,range(10))
    print(res)


# 6、回调函数
# 回调函数都是在主进程中执行，不能再多传参数，只能接收多进程中函数的返回值
# 应用：多进程的io多，多进程去拿数据，主程序执行
from multiprocessing import Pool
from multiprocessing import Process
import time
import os

def func(i):
    print('子进程：%s的pid为:%s'%(i,os.getpid()))
    i += 1
    return i

def callback_func(args):
    print('回调的进程pid为:%s'%(os.getpid()))
    print(args)

if __name__ == '__main__':
    print('主进程pid为:%s'%(os.getpid()))
    po = Pool(5)
    l = []
    for i in range(10):
        res = po.apply_async(func,args=(i,),callback=callback_func)
        l.append(res)
    po.close()
    # po.join()
    [po.join() for i in l]
'''
# 7、回调函数应用实例
# 我们请求网页的时候肯定是有网络延迟，也就是有io操作
# 如果使用单进程访问10个页面，那么在等待的时候耗费的最多时间
# 所以，使用多进程同时访问10个页面，那么我等待了1s有可能就有一个值，谁先返回就去处理，这里就可以使用多进程
# 分析处理页面的返回结果，就可以使用回调函数，假如分析页面的长度
# from urllib.request import urlopen
import requests              # 该模块是对urllib模块的封装
from multiprocessing import Pool
# res = requests.get('https://www.baidu.com')
# print(res)
# print(res.text)                   # 网页源代码
# print(res.status_code)              # 返回的状态码

def get_url(url):
    res = requests.get(url)
    return {'status_code':res.status_code,
            'content':res.text,
            'url':url}
def analysis(args):
    print(args['url'],args['status_code'],len(args['content']))

if __name__ == '__main__':
    po = Pool(5)
    url_list = ['http://www.baidu.com',
                'http://www.taobao.com',
                'http://www.hao123.com',
                'http://www.sogou.com',
                'https://www.qq.com/',
                'https://www.python.org/']
    for url in url_list:
        po.apply_async(get_url,args=(url,),callback=analysis)
    po.close()
    po.join()

# http://www.baidu.com 200 2381
# http://www.sogou.com 200 24220
# https://www.qq.com/ 200 221566
# http://www.taobao.com 200 133343
# http://www.hao123.com 200 296619
# https://www.python.org/ 200 49646