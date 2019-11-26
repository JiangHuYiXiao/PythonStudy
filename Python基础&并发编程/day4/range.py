# -*- coding:utf-8 -*-
# range() 函数可创建一个整数列表，一般用在 for 循环中。

# 格式1：
for i in range(1,100):
    print(i)
# 格式2：
for i in range(50,100):
    print(i)
# 格式3：
for i in range(100):
    print(i)

# 可以使用步长
for i in range(1,100,2):
    print(i)

# 倒序
for i in range(10,0,-2):  #-1，或者步长为负数都是代表是按照倒着取，（100,0）表示取出来是倒序排列
    print(i)               #第三个数为负数，则第1、2个数也要倒序，先大后小，否则，输出i什么也没有

for i in range(0,100,-2):
    print(i)   #什么都没有

for i in range(0,10,-2):
    print(i)     #什么都没有

# 练习题：循环取出列表li中的所有元素包括子列表中的元素都要一一输出
li = [1,2,3,5,'alex',[2,3,4,5,'taibai'],'afds']
for i in li:
    if type(i) == list:
        for k in i:
            print(k)
    else:
        print(i)


