# -*- coding:utf-8 -*-

# 一、列表推导式

'''
#一个简易的列表推导式：
res = [i for i in range(30)]    # -----相当于一个遍历功能
print(res)              # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]


# 练习1：30以内所有被3整除的数
# 完整的一个列表推导式:
# 条件成立后的结果或者继续操作结果 for i in 可迭代对象 if 条件成立    -----相当于一个筛选器
res = [i for i in range(30) if i%3 ==0]
print(res)              # [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]


# 练习2：30以内所有被3整除的数的平方

res = [i* i for i in range(30) if i%3 == 0]
print(res) # [0, 9, 36, 81, 144, 225, 324, 441, 576, 729]

# 练习3：找到嵌套列表中名字含有两个‘e’的所有名字
names = [['Tom', 'Billy', 'Jefferson', 'Andrew', 'Wesley', 'Steven', 'Joe'],
         ['Alice', 'Jill', 'Ana', 'Wendy', 'Jennifer', 'Sherry', 'Eva']]

res = [name for list in names for name in list if name.count('e')==2]
print(res)   # ['Jefferson', 'Wesley', 'Steven', 'Jennifer']
'''

# 二、字典推导式
# 练习1：将一个字典的key和value对调
mcase = {'a': 10, 'b': 34}
res = {mcase[k]:k for k in mcase}
print(res)    # {10: 'a', 34: 'b'}

# 练习2：合并大小写对应的value值，将k统一成小写
mcase = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}
res = {k.lower():mcase.get(k.lower(),0) + mcase.get(k.upper(),0) for k in mcase}  # 不设置get后面为0则可能出现int+None
print(res)          # {'a': 17, 'b': 34, 'z': 3}
