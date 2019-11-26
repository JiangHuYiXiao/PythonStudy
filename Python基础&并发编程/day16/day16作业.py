# -*- coding:utf-8 -*-

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

# 6、如下，每个小字典的name对应股票名字，shares对应多少股，price对应股票价格。
portfolio=[
    {'name':'IBM','shares':100,'price':91.1},
    {'name':'AAPL','shares':50,'price':543.22},
    {'name':'FB','shares':200,'price':21.09},
    {'name':'HPQ','shares':35,'price':31.75},
    {'name':'YHOO','shares':45,'price':16.35},
    {'name':'ACME','shares':75,'price':115.65}
]
    # 6.1计算购买每只股票的总价
    # 6.2用filter过滤出，单价大于100的股票有哪些
# 6.1
# 方法1：
def sum_price():
    for i in portfolio:
        s_price = round(i['shares']*i['price'],2)
        s_name = i['name']
        print(s_name,'总价:',s_price)
sum_price()

# 方法2：
def sum_price(dict):
        return dict['shares']*dict['price']
res = map(sum_price,portfolio)
for a in res:
    print(a)

# 方法3:
sum_price = map(lambda dict:dict['shares']*dict['price'],portfolio)
for i in sum_price:
    print(i)

# 6.2
# 方法1：
def price_100(a):
    if a['price'] > 100:
        return a
res = filter(price_100,portfolio)
for i in res:
    print(i)
# 方法2：
res = filter(lambda dict: dict['price']>100,portfolio)
for i in res:
    print(i)




