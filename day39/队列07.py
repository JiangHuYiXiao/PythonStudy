# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/11/20 17:32
# @Software       : Python_study
# @Python_verison : 3.7
'''

# 1、queue    先进先出是队列
import queue
Q = queue.Queue()           # 线程中安全的队列,先进先出
Q.put('hello')
Q.put(111)
print(Q.get())
print(Q.get())


# 2、LifoQueue    后进来的先出来,就是栈
import queue
qlf = queue.LifoQueue()
qlf.put(1)
qlf.put(2)
qlf.put(3)
qlf.put(4)
print(qlf.get())            # 4
print(qlf.get())            # 3
print(qlf.get())            # 2
print(qlf.get())            # 1

'''
# 3、PriorityQueue   优先级，值越小，越优先,值相同则先进先出
import queue
pq = queue.PriorityQueue()
pq.put((1,'cc'))
pq.put((1,'dc'))
pq.put((10,'bb'))
pq.put((23,'aa'))
pq.put((12,'dd'))
print(pq.get())
print(pq.get())
print(pq.get())
print(pq.get())
print(pq.get())