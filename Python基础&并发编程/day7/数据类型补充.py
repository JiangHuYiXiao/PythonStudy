# -*- coding:utf-8 -*-
# str补充
str = 'a'
str1 = ' '
# 1、判断字符串是否全部是空格
print(str.isspace())

print(str1.isspace())

# list补充
# 2、在循环中对列表进行删除，结果会出错，或者报错，因为随着循环，列表的元素被删除，列表的元素在减少，所以会出现索引越界。
# 所以再以后的工作中，我们不要在循环的时候对列表进行删除
# 举例如下:
# 例子1
list = [11,12,13,14,15]
for i in list:
    print(i)
    del(list[i])    #IndexError: list assignment index out of range
    print(list)

# 例子
for i in range(len(list)):
    print(i)
    del(list[i])
    print(list)
# i     list
# 0     [12, 13, 14, 15]
# 1     [12, 14, 15]    删除错了，因为元素减少了，应该是删除12的，而不是删除13
# 2     [12, 14]        删除错了，因为元素减少了，应该是删除13的，而不是删除15
# 3     索引最多是1，但是这边要去查找3，所以报错，提示索引越界


# 需求：用两种方法把列表中索引为基数的数删除
# 方法1
list1 = list[::2]
print(list1)


# 方法2
list2 = []
for i in list:
    if list.index(i) % 2 == 0:
        list2.append(i)
list = list2
print(list)

# 3、连续赋值，公用一个内存地址
a = 1
b = a
c = a
print(a is b is c)
print(a,b,c)   # 1 1 1

l1 = []
l2 = l1
l3 = l1
l3.append('a')
print(l1 is l2 is l3)
print(l1,l2,l3)   # ['a'] ['a'] ['a']



# 4、添加多个相同数据到列表中
print(['1' for i in range(4)])

print([12 for i in range(4)])


# 5、各个数据类型转换为bool值为False的值
# false
print(bool(0))  #int
print(bool())   #str
list3 = []
print(bool(list3))  #list
tuple = ()
print(bool(tuple))  #tuple
dict = {}
print(bool(dict))   #dict
set = {}
# print(bool(set))    #set

# 6、如果元组里面只有一个元素且不加逗号那么此元素的数据类型是什么类型就是什么类型
tuple = (1)
print(type(tuple))   #<class 'int'>

tuple1 = ('1')
print(type(tuple1))   #<class 'str'>

tuple2 = (1,)
print(type(tuple2))  # <class 'tuple'>


# dict补充
# 7、在循环的时候对字典进行删除
# 需求：删除字典dict = {}的key值中含有k元素的键值对

dict = {'k1':'v1','k2':'v2','k3':'v3','a3':'v3'}
dict2 = {}
# 报错代码
for i in dict:   # dictionary changed size during iteration
    if 'k' in i:
        del(dict[i])
# 方法1
for i in dict:
    if 'k' not in i:
        dict2.setdefault(i,dict[i])
dict = dict2
print(dict)


# 方法2:将键值含有k的都添加到一个列表中，然后循环列表，删除字典的键值对
li = []
for i in dict:
    if 'k' in i:
        li.append(i)
print(li)
for i in li:
    del(dict[i])
print(dict)

# 8、根据键值，批量生成值

dic = dict.fromkeys([11,22,13],'jianghu')
print(dic)   #{11: 'jianghu', 22: 'jianghu', 13: 'jianghu'}

dic = dict.fromkeys([11,22,13])
print(dic)   #{11: None, 22: None, 13: None}

dic = dict.fromkeys([11,22,13],[])
print(dic)   #{11: [], 22: [], 13: []}




























