#-*- coding:utf-8 -*-
# 一、函数的定义
# 定义：def 函数名（）

# 假设，len（）函数，不能使用了，需要你自己开发一个计算数据长度的函数
s = '人生苦短'
def my_len():           #函数的定义
    i = 0
    for k in s:
        i += 1
    print(i)
res = my_len()          #函数的调用
print(res)              #返回值为None,因为这个函数没有返回值

# 二、函数的调用
# 调用：函数名（）


# 三、函数的返回值
# return的作用:
# 1、返回值，
# 2、也代表结束函数
# 3、有返回，则必须要有接收，不接收则获取不到返回值
# 4、如果程序有多个return，则只会执行第一个return

s1 = '人生苦短'
def my_len():
    i = 0
    for k in s:
        i = i + 1
    return i
res = my_len()
print(res)

# 返回值的情况
# 1、没有返回值（没有return，有return返回但是为空，return None）
# 2、返回一个值
# 3、返回多个值

# 需求：定义一个求和函数


# 1、没有返回值，没有return
# 函数体内如果出现return，则后面的函数体内语句不再执行，
def my_sum():
    a = 1
    b = 2
    c = a + b
res = my_sum()
print(res)     #None

# 2、有返回值，return为空
def my_sum():
    a = 1
    b = 2
    c = a + b
    return
    # print('结束')  #不执行
res = my_sum()
print(res)

# 3、有返回值，return None（最不常用）
def my_sum():
    a = 1
    b = 2
    c = a + b
    return None
res = my_sum()
print(res)


# 4、返回一个值，可以返回任意数据类型
def my_sum():
    a = 1
    b = 2
    c = a + b
    return c
res = my_sum()
print(res)

def func():
    return[1,2,3]
print(func())


def func():
    return{'a':1,'b':2,'c':3}
print(func())

def func():
    return{'a':1,'b':2,'c':3}
    return (22,33)    #不执行，如果程序有多个return，则只会执行第一个return
print(func())

# 5、返回多个值
# 用一个接收，返回结果为一个元组
def my_sum():
    a = 1
    b = 2
    c = a + b
    return c,a,b
res = my_sum()
print(res)      # (3, 1, 2)

# 有多少返回值，用多少接收

def my_sum():
    a = 1
    b = 2
    c = a + b
    return c,a,b
res1,res2,res3 = my_sum()
print(res1,res2,res3)    #3 1 2

# 有三个返回值，不能用多余三个，接收，也不能用少用3个接收，1个接收除外

def my_sum():
    a = 1
    b = 2
    c = a + b
    return c,a,b
res1,res2 = my_sum()
print(res1,res2)    #ValueError: too many values to unpack (expected 2)


def my_sum():
    a = 1
    b = 2
    c = a + b
    return c,a,b
res1,res2,res3,res4 = my_sum()
print(res1,res2,res3,res4)    #ValueError: too many values to unpack (expected 2)

# 函数的参数
# 1、无参数
s = '人生苦短'
def my_len(a):           #函数的定义
    i = 0
    for k in s:
        i += 1
    print(i)
res = my_len()          #函数的调用
print(res)              # TypeError: my_len() missing 1 required positional argument: 'a'

# 2、有参数
# 实参为str
def my_len(s):           #函数的定义,s是形参，或者接收参数
    i = 0
    for k in s:
        i += 1
    return i
res = my_len('wo')          #函数的调用，‘wo’是实参或者传参
print(res)              #2

# 实参为list
def my_len(s):           #函数的定义
    i = 0
    for k in s:
        i += 1
    return i
res = my_len([1,2,3,4])          #函数的调用
print(res)       #4
# 参数：
# 1、无参数
# 2、一个参数
# 3、多个参数
def my_sum(a,b):
    res = a + b
    return res
print(my_sum(1,3))


# 站在形式参数的角度（也就是函数定义的时候），参数的分类以及参数的定义顺序

# 1、位置参数：必须传，且有几个参数传几个
# 2、*args：动态参数，多个位置参数
# 3、默认参数:如果不传，则用默认的，传了用传的
# 4、**kwargs：动态参数，多个默认参数




# *args 动态参数，多个位置参数
def my_sum(*args):
    n = 0
    for i in args:
        n = n + i
    return n
print(my_sum(1,3))
print(my_sum(1,3,65,756))

# 默认参数a,b
def my_sum(a,b=1):
    res = a + b
    return res
print(my_sum(a=3))
print(my_sum(a=3,b=3))

# *kwargs 动态参数可以接收多个任意参数，站在实参的角度为多个关键字参数,返回一个字典
def my_sum(**kwargs):
    print(kwargs)
my_sum(a=1,b=3)
my_sum(a=1,b=3,c=65,d=756)

# 混合用，可以是接收任意多个参数，不过位置参数在前面，也就是args必须在kwargs之前
def my_sum(*args,**kwargs):
    print(args,kwargs)
my_sum(12,a=1,b=3)
my_sum(11,a=1,b=3,c=65,d=756)

# 站在实际参数的角度（也就是函数调用的时候），参数的分类以及参数的顺序

# 1、按照位置传参数
# 2、按照关键字传参数
# 3、混着用，也可以，但是必须是位置参数在前面
#
# # 1、位置参数a,b
def my_sum(a,b):
    res = a + b
    return res
print(my_sum(1,3))    #1、实参为位置参数
# # 2、关键字参数a,b
def my_sum(a,b):
    res = a + b
    return res
print(my_sum(a=1,b=3))    #2、实参为关键字参数

# # 3、混着用，也可以，但是必须是位置参数在前面
def my_sum(a,b):
    res = a + b
    return res
print(my_sum(1,b=3))

def my_sum(a,b):
    res = a + b
    return res
# print(my_sum(a=1,3))    #2、报错，位置参数在前


# 动态参数的另一种表现形式
def func(*args):  # 站在形参的角度，给变量加上*就是组合所有传来的值
    print(args)
func(2,3,4,5,6)                # 站在实参的角度，给list加上*就是按照顺序打散这个序列
l=[2,3,4,5,6]
func(*l)

def func(**kwargs):  # 站在形参的角度，给变量加上**就是组合所有传来的值
    print(kwargs)
func(a=2,b=3)                # 站在实参的角度，给dict加上**就是按照顺序打散这个字典
dic={'a':2,'b':3}
func(**dic)
