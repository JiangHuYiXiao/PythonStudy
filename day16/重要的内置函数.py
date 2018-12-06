# -*- coding:utf-8 -*-
# len()计算长度
# enumerate()枚举
# all()判断是否全部为True,全为真，则返回真
# any()判断是否有任意一个为True，有一个为真，则返回真
# zip()拉链方法

print(all([1,2,0,'',[]]))           # False
print(all([1,2,0,[]]))           # True

print(any([1,2,0,[]]))           # True
print(any([(),'']))           # False

l1=[12,14,13]
l2=['a','b','c']
t1 = (1,'12')
dict1 = {23,3242,345,234324,4323224}
print(zip(l1,l2))    # <zip object at 0x0000000002857B08> 迭代器
for i in zip(l1,l2):
    print(i)
# (12, 'a')
# (14, 'b')
# (13, 'c')

print(zip(l1,l2,t1,dict1))
for i in zip(l1,l2,t1,dict1):
    print(i)
# (12, 'a', 1, 3242)
# (14, 'b', '12', 234324)