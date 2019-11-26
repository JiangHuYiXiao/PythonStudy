#-*- coding:utf-8 -*-
# 函数名 = lambda 参数:函数体   （只能写一行）
# 匿名函数可以有名字
# 比如：calc = lambda n:n**n，函数名为calc，
# 到目前为止，我们所学到的内置函数其中含有key关键字的有：（max，min，map，filter，sorted）
# 然后这五个函数都可以和lambda集合进行使用

calc = lambda n:n**n
print(calc(10))
# 一、匿名函数和普通函数的转换
# 练习1：把下面的函数改成匿名函数
def add(x,y):
    return x+y
print(add(2,3))

add = lambda x,y:x+y
print(add(12,21))

# 二、lambda和max结合使用
# 需求1：筛选出字典中value值最大的key值
dict = {'k1':11,'k2':210,'k3':20}
def func(key):
    return dict[key]
print(max(dict,key=func))

# 使用匿名函数
print(max(dict,key=lambda key:dict[key]))

# 三、lambda和filter结合使用，一般用在返回的元素个数少于等于使用前元素的个数
# 练习2：筛选列表中大于10的数[5,8,11,9,15]
def func(num):
    if num>10:
        return num
res = filter(func,[5,8,11,9,15])
print(res)
for i in res:
    print(i)

# 使用匿名函数

res = filter(lambda num:(num > 10),[5,8,11,9,15])
for i in res:
    print(i)

#四、lambda和map结合使用一般用在返回的元素个数和使用前是一样的情况
# 练习3：求列表中各个元素的平方根[1,5,7,4,8]
list = [1,5,7,4,8]
# double = lambda num:num*num
res = map(lambda num:num*num,list)
for i in res:
    print(i)

# 面试题1：下面程序的输出结果是
d = lambda p:p*2
t = lambda p:p*3
x = 2
x = d(x)    # 4
x = t(x)    # 12
x = d(x)    # 24
print(x)
# 这个就是一个连续赋值的过程对x，最终x =24

# 面试题2：现有两个元组(('a'),('b')),(('c'),('d')),请使用python中的匿名函数生成列表[{'a':'c'},{'b':'d'}]
tuple1 = (('a'),('b'))
tuple2 = (('c'),('d'))
res = zip(tuple1,tuple2)
# def func(x):
#     return {x[0]:x(1)}
ret = map(lambda x:{x[0]:x[1]},res)   # lambda x:{x[0]:x[1]} for i in res
print(list(ret))  # 通过强制转换的方式可以从一个可迭代对象里面取值

# 面试题3：以下代码的输出是什么，并给出答案,请修改multipliers的定义来产生期望的结果
# def multipliers():
#     return [lambda x :i*x for i in range(4)]
# print([m(2) for m in multipliers()])

def multipliers():
    return [lambda x: i * x for i in range(4)]
    # 等价于return [lambda x :0*x，lambda x :1*x，lambda x :2*x，lambda x :3*x]
print([m(2) for m in multipliers()])
# multipliers()这个是调用函数 multipliers()
# [m(2) for m in multipliers()]这个是一个列表推导式，返回m（2）m就是lambda函数lambda x：3*x x=2  6
# res = [6,6,6,6]