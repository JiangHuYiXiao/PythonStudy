#-*- coding:utf-8 -*-
# 1、装饰器的形成

# V1

def func():# 被装饰的函数：

    print('你好我好大家好')

# 函数调用
func()


# 现在需要添加计算出func函数执行的时间
# 则改为
# V2
import time
def func():
    start = time.time()
    print('你好我好大家好')
    time.sleep(0.01)   #如果不加则时间太短了，无法统计，所以加个sleep然后减去就可以了得到func函数执行时间
    end = time.time()
    sum_time = end - start
    print(sum_time)

func()   #0.010000228881835938


# V3
# 如果需要对之前所有的函数都加上这个计算时间的功能，不可能每个函数都去添加，太麻烦了
# 所以新增一个函数,这个函数的功能就是用来计算函数执行的时间的

import time
def timer(f):                # 装饰器函数
    start = time.time()
    f()                      # 这个位置需要添加调用func函数，所以需要在这添加函数调用，
                            # 但是这个函数名怎么来呢，所以就需要我们timer函数有入参
    end = time.time()
    print(end-start)


def func():                #被装饰的函数
    time.sleep(0.01)
    print('你好我好大家好')


# 调用func函数，实际上是调用timer函数，不过就是添加了计算时间的功能
# timer(func)     # 0.010000467300415039

# 按照这样修改的话，以后需要调用func的时候，都需要改成调用timer，这样对于
# 以前调用过func的代码，都需要修改，太麻烦了，
# 最终，我们还是希望让他们调用func，这样就是希望他们在调用timer的时候，调用的是func就完美了
# 可以把timer的内存地址赋值给func
# func = timer
# func()   # 这里其实是调用timer，所以需要参数，参数应该是传func的内存地址，这样就需要在调用timer的时候返回func的内存地址
# 这就需要用到闭包，内部函数使用外部函数的变量

# V4
def func():                   #被装饰的函数 ，步骤2
    time.sleep(0.01)          # 步骤10
    print('你好我好大家好')     #步骤11


import time
def timer(f):                 # 装饰器函数 ，步骤1
    def inner():              # 步骤 4
        start = time.time()   # 步骤 8
        f()                   #这个f就是外部函数的变量，所以inner函数是一个闭包函数，步骤9，调用func
        end = time.time()     # 步骤12
        print(end-start)      # 步骤13
    return inner              #步骤 5 返回inner名字的内存地址不能加括号


# 调用函数
# func = timer(func)   # 这里现在func的值是inner的内存地址  ，赋值右边，步骤3   赋值左边步骤6，把inner的内存地址返回给func
# func()           #步骤7，调用inner函数，这里面的func都要是被装饰的函数名

# 这个timer就是一个简单的装饰器，装饰器函数需要有内部函数，且内部函数，
# 且需要返回内部函数的函数名
# 调用装饰器函数timer，传参为被装饰的函数的函数名，然后将装饰器函数返回的内部函数inner的内存地址赋值给被装饰的函数
# 这个时候函数名func其实是内部函数inner的内存地址，调用func，实质是调用inner，然后在inner里面实际上却又会调用func函数
# 不想修改原来的函数的调用方式，但是还是想在原来函数上的前后名添加功能，
# 这个时候就需要用到装饰器函数，

# 2、开放封闭原则
# 开放：对添加扩展是开放的
# 封闭：对修改是封闭的
