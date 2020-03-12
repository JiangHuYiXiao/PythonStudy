# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/3/12 15:15
# @Software       : Python_study
# @Python_verison : 3.7

def func(m):
    for k,v in m.items():
        m[k+2] = v+2

m = {1: 2, 3: 4}
l = m  # 浅拷贝
l[9] = 10
# func(l)     # RuntimeError: dictionary changed size during iteration
m[7] = 8

# 请问最后，l和m的值是多少
# 1、知识点，遍历字典时，不允许继续对key进行操作,只能对value进行操作
# 2、深浅copy,

# 浅copy，同一个内存地址
import copy
l1 = [1,2,3,[4,5]]
l2 = l1.copy()

# 深copy，不同的内存地址
list1=[1,2]
list2=copy.deepcopy(list1)

# 注释func(1)后
print("l",l)
print("m",m)
l={1:2,3:4,9:10,7:8}
m={1:2,3:4,9:10,7:8}
