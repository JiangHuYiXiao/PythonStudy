#-*- coding:utf-8 -*-
# 1、写函数，检查获取传入列表或者元组对象所有奇数的位索引对应的元素，并将其作为新列表返回给调用者。
'''
方法1：
def func(*args):
    list = []
    for i in args:
        index = args.index(i)
        if index % 2 == 1:
            list.append(i)
    return list
# 调用函数
res = func(2,3,1,5,6,9,4)
print(res)

res = func(*[1,3,5,6,7])
print(res)

# 方法2：
def func(args):
    list = []
    for i in args:
        index = args.index(i)
        if index % 2 == 1:
            list.append(i)
    return list
# 调用函数
res = func((2,3,1,5,6,9,4))
print(res)

res = func([1,3,5,6,7])
print(res)
'''
# 2、写函数，判断用户传入的对象（字符串，列表，元组）长度是否大于5
'''
def func2(args):
    k = 0
    for i in args:
        k += 1
    if k > 5:
        return True
    else:
        return False
res1 = func2('sdjfoiwe')
res2 = func2('sd')
res3 = func2([1,2,43,543])
res4 = func2([1,2,3,4,5,6])
res5 = func2((1,2,3,4,5,6,7))
print(res1,res2,res3,res4,res5)
'''

# 3、写函数，检查传入列表的长度，如果大于2，那么保留前两个长度的内容，并将新内容返回给调用者