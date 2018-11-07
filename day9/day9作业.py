#-*- coding:utf-8 -*-
# 1、写函数，检查获取传入列表或者元组对象所有奇数的位索引对应的元素，并将其作为新列表返回给调用者。
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
