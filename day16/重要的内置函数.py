# -*- coding:utf-8 -*-
# len()计算长度
# enumerate()枚举
# all()判断是否全部为True,全为真，则返回真
# any()判断是否有任意一个为True，有一个为真，则返回真
# zip()拉链方法
# filter(func名称,可迭代对象)过滤器方法
'''
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
'''

def is_odd(num):
    if num%2 == 1:
        return(num)

res = filter(is_odd,[1,2,34,3,18])     # 等价于[i for i in [1,2,34,3,18] if i%2 ==1]
print(res)          # <filter object at 0x00000000022985F8>
for i in res:
    print(i)        # 1,3

# 练习1：筛选出列表中比10大的数字[12,122,2,34,9,6,4]
list = [12,122,2,34,9,6,4]
def compare_func(num):
    if num > 10:
        return num
res = filter(compare_func,list)
for i in res:
    print(i)

# 练习2：筛选出列表中的字符串
list1 = [12,'jianghu',2,'abc',9,6,4]
def str_func(num):
    if type(num) == str:
        return num
res = filter(str_func,list1)
for i in res:
    print(i)

# 练习3：删除None或者空字符串
list2 = [12,'jianghu',2,'abc',None,'',4]
def is_none(s):

        return s and str(s).strip()
for i in filter(is_none,list2):
    print(i)
