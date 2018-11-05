# -*- coding:utf-8 -*-
# 1.注册登录购物系统,用户名和密码通过input获取存入到文件中，然后对比文件中和输入的是否一致，一致登录成功，不一致登录失败。







# 2. 文件a.txt内容：每一行内容分别为商品名字，价钱，个数。
'''
apple 10 3
tesla 100000 1
mac 3000 2
lenovo 30000 3
chicken 10 3
# 通过代码，将其构建成这种数据类型：[{'name':'apple','price':10,'amount':3},{'name':'tesla','price':1000000,'amount':1}......] 并计算出总价钱。

list = []
with open('a',mode = 'r+',encoding='utf-8') as file:
    for i in file:
        ls = i.strip().split()
        dic = {'name':ls[0],'price':ls[1],'amount':ls[2]}
        list.append(dic)
print(list)

list = [{'name': 'apple', 'price': '10', 'amount': '3'}, {'name': 'tesla', 'price': '100000', 'amount': '1'}, {'name': 'mac', 'price': '3000', 'amount': '2'}, {'name': 'lenovo', 'price': '30000', 'amount': '3'}, {'name': 'chicken', 'price': '10', 'amount': '3'}]

# 方法1
price = 0
for count in range(len(list)):
    price += int(list[count]['price'])*int((list[count]['amount']))
print(price)

# 方法2
price = 0
for count in list:
    price += int(count['price'])*int(count['amount'])
print(price)
'''

'''
# 3.有如下文件：

# ------
alex是老男孩python发起人，创建人。
alex其实是人妖。
谁说alex是sb？
你们真逗，alex再牛逼，也掩饰不住资深屌丝的气质。
# ------
# 将文件中所有的alex都替换成大写的SB
'''

with open('alex',mode='r+',encoding='utf-8') as file:
    i = 0
    list = file.readlines()
    while i < len(list):
        list[i].strip().replace('alex','SB')
    print(file.read())


