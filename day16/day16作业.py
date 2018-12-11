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
'''
# 5、随意写一个20行的文件，
# 运行程序，先将内容读到内存里面，用列表存储。
# 接收用户的输入页码，每页五条，仅仅输出当页的内容
with open('article',mode='r+',encoding='utf-8') as file:
    list1 = file.readlines()
input_page = int(input('请输入你的页码：'))
tup1 = divmod(len(list1),5)
if tup1[1] ==0:
    cal_page =tup1[0]
else:
    cal_page= tup1[0]+1
if input_page<= cal_page and input_page >=1:
    res = (list1[5*(input_page-1):input_page*5])
    for i in res:
        print(i.strip())
elif input_page > len(list1) / 5:
    print('超过最大页码:%s'%(cal_page))
else:
    print('页码不能小于1')
