# -*- coding:utf-8 -*-
# 1、判断下列逻辑语句为True或者False
# 优先级：() > not > and > or
# a = 1 > 1 or 3 < 4  or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6      #True
#
# b = (not 2 > 1 and 3 < 4  or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6)     #False
#
# c = (1 > 2 and 3 < 4  or 4 > 5 and 2 > 1 and 9 < 8 and 4 > 6 or 3 < 2)     #False
# print(a,b,c)
#
# # 2、求出下列逻辑语句的值
# d = 8 or 3 and 4 or 2 and 0 or 9 and 7           # 8
# e = 0 or 2 and 3 and 4 or 6 and 0 or 3           # 4
# f = 5 and 9 or 10 and 2 or 3 and 5 or 4 or 5     # 9
# print(d,e,f)
# #规律：先not后and后not，
# # and 如果第一个为真的话取后面一个值，因为一个为真不能判断整个表达式为真，只有两个为真才为真。
# # and 如果第一个为假，则返回第一个
# # or取第一个非0的值
#
# # 3、下列的结果是什么？
# g = 6 or 2 > 1  # 6
# h = 3 or 2 > 1  # 3
# i = 0 or 5 < 4  # False
# j = 5 < 4 or 3  # 3
# k = 2 > 1 or 6  # True
# l = 3 and 2 > 1 # True
# m = 0 and 3 > 1 # 0
# n = 2 > 1 and 3 # 3
# o = 3 > 1 and 0 # 0
# p = 3 > 1 and 2 or 2 < 3 and 3 and 4 or 3 > 2   # 2
# print(g,h,i,j,k,l,m,n,o,p)

# 4、简述变量命名规范
# 只能由字母、数字、下划线的任意组合组成。
# 数字不能开头
# 尽量做到见名知意
# 不能是Python中的关键字
# 一般使用下划线这种格式，不使用驼峰样式

# 5、name = input('请输入你的名字：')中name的数据类型是？
# input输出的数据类型默认为str

# 6、if条件语句的基本结构
'''
1、没得选
if 条件:
    结果
    
2、二选一
if 条件:
    结果
else：
    结果

3、多选一
if 条件:
    结果
elif 条件:
    结果
elif 条件:
    结果
else:
    结果
    
4、if嵌套 
if 条件：
    if 条件：
        结果
    else：
        结果
else：
    结果     

'''
# 7、while循环语句基本结构
'''
while 条件：
    循环体
    终止循环（没有终止循环则为死循环，
            终止循环有两种方式：
            改变条件或者
            break：终止整个循环
            continue：终止本次循环，会执行下次循环）
'''
# 8、写代码计算1-2+3...+99中除了88以外的所有数的和。
count = 0
sum = 0
while count <= 98:
    count = count + 1
    if count % 2 == 1:
        sum = sum + count
    else:
        if count == 88:
            continue
        sum -= count
print(sum)
