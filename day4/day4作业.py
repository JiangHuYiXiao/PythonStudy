#-*- coding:utf-8 -*-
# 1、写代码，有如下列表按照要求实现每一个功能
# li = ['alex','wusir','eric','rain','alex']

'''
# 1)计算列表的长度并输出
print(len(li))

# 2)在列表中追加元素seven，并输出添加后的列表
li.append('seven')
print(li)

# 3)请在列表的第一个位置添加'Tony'，并输出添加后的列表
li.insert(0,'Tony')
print(li)

# 4)请修改列表第二个位置的元素为‘Kelly',并输出修改后的列表
li[1] = 'Kelly'
print(li)

# 5)请将列表l2 = [,1,'a',3,4,'heart'] 的每一个元素添加到li中，一行代码实现，不允许循环添加
li.extend([1,'a',3,4,'heart'])
print(li)

# 6)请将字符串s = 'qwert' 的每一个元素添加到li中，一行代码实现，不允许循环添加
li.extend('qwert')
print(li)

# 7)请删除列表中的元素'eric',并输出删除后的列表
li.remove('eric')
print(li)

# 8)请删除列表中第二个的元素,并输出删除的元素和删除后的列表
print(li.pop(1))
print(li)


# 9)请删除列表中第二个至第四个元素,并输出删除后的列表
del(li[1:4])
print(li)

# 10)请列表的所有元素反转,并输出反转后的列表
li.reverse()
print(li)

# 11)请计算出‘alex’在列表中出现的次数,并输出该次数
print(li.count('alex'))
'''

# 2、写代码，有如下列表，利用切片实现每一个功能
# li = [1,3,2,'a',4,'b',5,'c']
'''
# 1)通过对li切片形成新的列表l1,l1 = [1,3,2]
l1 = (li[0:3])
print(l1)

# 2)通过对li切片形成新的列表l2,l2 = ['a',4,'b']
l2 = li[3:6]
print(l2)

# 3)通过对li切片形成新的列表l3,l3 = [1,2,4,5]
l3 = li[0::2]
print(l3)

# 4)通过对li切片形成新的列表l4,l4 = [3,'a','b']
l4 = li[1:6:2]
print(l4)

# 5)通过对li切片形成新的列表l5,l5 = ['c']
l5 = li[-1]
print(l5)

# 6)通过对li切片形成新的列表l6,l6 = ['b','a',3]
l6 = li[5:0:-2]
print(l6)
'''
# 3、写代码，有如下要求，按照要求实现每一个功能

lis = [2,3,'k',['qwe',20,['k1',['tt',3,'1'],89]],'ab','adv']


# # 1)将列表中的tt变成大写（用两种方式）
# lis[3][2][1][0] = (lis[3][2][1][0].upper())
# print(lis)
#
# lis[3][2][1][0].replace('tt','TT')
# print(lis)
#
#
# # 2)将列表中的3变成字符串‘100’（用两种方式）
# # 方法1
# lis[1] = '100'
# lis[3][2][1][1] = '100'
# print(lis)
#
# # 方法2
# lis.remove(3)
# lis.insert(1,'100')
# lis[3][2][1].remove(3)
# lis[3][2][1].insert(1,'100')
# print(lis)
#
# # 3)将列表中的1变成数字101（用两种方式）
# # 方法1：
# lis[3][2][1][-1] = 101
# print(lis)
#
# # 方法2
# lis[3][2][1][-1] = int(lis[3][2][1][-1] .replace('1','101'))
# print(lis)
#
# # 方法3
# lis[3][2][1][-1] = int(lis[3][2][1][-1]) + 100
# print(lis)
#
# # 方法4
# lis[3][2][1][-1] = lis[3][2][1][-1] + '01'
# print(lis)
#
# # 方法5
# lis[3][2][1][-1] = '10' + lis[3][2][1][-1]
# print(lis)
