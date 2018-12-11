# -*- coding:utf-8 -*-
'''
# 1、默写：
L = [1,2,3,4]
def pow2(x):
    return x*x

print(list(map(pow2,L)))            # [1,4,9,16]

def is_odd(x):
    return x%2 ==1
print(list(filter(is_odd,L)))       # [1,3]

# 2、所有标红色的、黄色的内置方法必须会用，每个方法用法敲一遍。
'''
# 3、用map来处理字符串列表，把列表中所有人变成sb，比如alex_sb。
name = ['alex','wupeiqi','yuanhao','nezha']
def sb_func(x):
    return x+'_sb'
print(list(map(sb_func,name)))

# 4、用filter函数来处理数字列表，将列表中的所有偶数筛选出来
num = [1,3,5,6,7,8]
def double_num(x):
    return x % 2 ==0
print(list(filter(double_num,num)))

# 5、随意写一个20行的文件，
# 运行程序，先将内容读到内存里面，用列表存储。
# 接收用户的输入页码，每页五条，仅仅输出当页的内容