# -*- coding:utf-8 -*-
# 1、装饰器的初成：
import time
def timer(func):   # 装饰器函数
    def inner():
        # '被装饰函数之前要做的功能'
        start = time.time()
        re = func()   #被装饰的函数
        # '被装饰函数之后要做的功能'
        time.sleep(0.01)
        end = time.time()
        print(end - start)
        return re
    return inner

def func():
    print('你好我好大家好！')
    return '老师好'

func = timer(func)
ret = func()
print(ret)



# 2、装饰器的最终形成：
import time    # 步骤 0
def timer(func):   # 步骤 1
    def inner(*args,**kwargs):   # 步骤 4
        # '被装饰函数之前要做的功能'
        start = time.time()   # 步骤 8
        re = func(*args,**kwargs)   # 赋值号右边，步骤 9 赋值号左边，步骤12，将‘老师好’赋值给re
        # '被装饰函数之后要做的功能'
        time.sleep(0.01)     # 步骤 13
        end = time.time()    # 步骤 14
        print(end - start)    # 步骤 15
        return re    # 步骤 16 将func的返回值‘老师好’返回给ret
    return inner    # 步骤 6
@timer    # func = timer(func) # 右边步骤 3 左边步骤 7
def func(*args,**kwargs):    # 步骤 2
    print('你好我好大家好！')    # 步骤 10
    return '老师好'    # 步骤  11

ret = func(1)    # 赋值号右边 步骤 7   赋值号左边 步骤17
print(ret)    # 步骤 18


# 3、装饰器的固定格式：
def wrapper(func):
    def inner(*args,**kwargs):
        '调用函数之前做的事'
        re = func(*args,**kwargs)
        '调用函数之后做的事'
        return re
    return inner

@wrapper
def func(*args,**kwargs):
    print('wahaha')
    return 'wahaha'

# 调用func
func = wrapper(func)  # 等价于在func上加上@wrapper
ret = func()
print(ret)


# 4、装饰器遵循的原则：开放封闭原则
#     a、对扩展是开放的
#     b、对修改是封闭的

# 5、语法糖 @被装饰函数名  放在装饰函数名上一行

# 6、参数问题学习
def outer(*args):   # 接收就是组合参数
    print(args)
    print(*args)    # 调用就是打散参数
    def inner(*args):   # 接收就是组合参数
        print('inner:',args)
    inner(*args)   # 调用就是打散参数


outer(1,2,3,4)
# (1, 2, 3, 4)
# 1 2 3 4
# inner: (1, 2, 3, 4)
