# -*- coding:utf-8 -*-
# 我们的数据类型按照是否可变可以划分为，可变数据类型，不可变数据类型

# 不可变数据类型:可以hash（hash是将特定的输入，通过hash算法输出）
# str,int,tuple,bool
# 可变数据类型：不可以hash
# list,dict,set
# 字典是python中唯一一个是按照键值对存在的数据类型，字典的key不可变，
# 但是value可变
# dic的查询是通过二分法进行查询，查询速度快

dic = {'name':'jianghu','age':17,'sex':'male'}

# 1、字典的增加
dic['height'] = 180   #在最后位置插入
print(dic)

dic['name'] = 'jiangxi' #如果key存在，则更新value值（这个是修改）
print(dic)

dic.setdefault('num',12)   #在最后位置插入
print(dic)

dic.setdefault('age',100) #如果key存在，不更新value值（这个是修改）
print(dic)

# 2、字典的删除

# 删除方法1：pop
dic.pop('name')   # 键如果存在则删除键和值，有返回值，返回删除的键对应的那个值，
print(dic.pop('name',20))   # 键如果不存在则返回后面的值，
print(dic)

dic.pop('age')
print(dic.pop('age'))      # 键如果不存在且后面没有填写值，则报错
print(dic)

dic.pop('hh')              # 键如果不存在且后面没有填写值，则报错
print(dic.pop('hash',213))   # 键如果不存在则返回后面的值，
print(dic.pop('wo','we'))    # 键如果不存在则返回后面的值，
print(dic)

# 删除方法2：popitem
dic.popitem()     #随机删除、
print(dic)

# 删除方法3：clear清空
dic.clear(dic)
print(dic)

# 删除方法4：delete删除
del(dic['name'])
print(dic)

# 3、字典的修改
dic['name'] = 'hehe'
print(dic)

# 修改方法2：通过对两个字典进行叠加update
dic2 = {'name':'yixiaojianghu','money':10000}
dic.update(dic2)   #把dic2的键值对更新到dic上，有就覆盖，没有则新增
print(dic)
print(dic2)

# 4、字典的查找

# 方法1：通过key查找
print(dic['name'])

# 方法2：通过get方法查找
print(dic.get('name'))

# 方法3：通过key查找字典的键
print(dic.keys())

# 方法4：通过key查找字典的值
print(dic.values())

# 方法5：通过key查找字典的键值
print(dic.items())    #返回的是列表，列表包含元组，元组再包含键值，

# 方法6：通过for循环查找字典的键
for i in dic:
    print(i)

for i in dic.keys():
    print(i)

for i in dic.values():
    print(i)

for i in dic.items():
    print(i)

# 面试题：
a = 1
b = 2
# 怎么样通过一行代码将a,b的值进行互换
a,b = b,a
a,b = [1,3],[2,4]
print(b,a)

# 方法7：通过for循环把字典打印出来，打印出来为字符串
for i,v in dic.items():
    print(i,v)