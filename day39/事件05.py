# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/11/20 9:40
# @Software       : Python_study
# @Python_verison : 3.7
# 事件就是阻塞，同时阻塞多个线程，也可以同时启用多个线程，和进程中的事件是一样的
# Event
# from threading import Event
# e = Event()
# e.wait()默认为阻塞
# e.set() 设置为非阻塞
# e.clear()设置为阻塞
# e.is_set() 为True时表示为非阻塞，为False表示阻塞

# 需求：使用多线程和事件实现，链接mysql数据库，最多链接3次，每次等待0.5秒,先进行检测，后进行链接、

from threading import Event
import time
import random
from threading import Thread

def check_conn():
    time.sleep(random.randint(1,2))     # 模拟检测时间
    # print(res)
    e.set()          # 非阻塞
    print(e.is_set())
def conn():
    count = 1
    print(e.is_set())
    while not e.is_set():           # 循环次数不限，for循环次数有限
        if count > 3:
            raise TimeoutError
        else:
            print('尝试连接第%s次'%(count))
        count += 1
        e.wait(0.5)             # 默认为阻塞，也就是e.is_set为False
    print('连接成功')


e = Event()
t1 = Thread(target=check_conn)
t1.start()
t2 = Thread(target=conn)
t2.start()