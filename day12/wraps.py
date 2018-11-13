# -*- coding:utf-8 -*-
# 1、需求想要获取holiday的函数名，注释文件等内置的方法，怎么获取？
from functools import wraps
def wrapper(func):  #func = holiday
    @wraps(func)
    def inner(*args,**kwargs):
        '''这个是inner函数'''
        print('在被装饰的函数执行之前做的事')
        ret = func(*args,**kwargs)
        print('在被装饰的函数执行之后做的事')
        return ret
    return inner

@wrapper   #holiday = wrapper(holiday)
def holiday(day):
    '''这是一个放假通知'''
    print('全体放假%s天'%day)
    return '好开心'


# 由于holiday现在是inner，所以直接使用返回的是
# print(holiday.__name__)     # inner
# print(holiday.__doc__)     # 这个是inner函数

# 这个时候就需要给装饰器本身再装饰使用wraps
from functools import wraps  # 导入ｗｒａｐｓ
# 在inner函数上一行加入待参数的装饰器@wraps（func）

print(holiday.__name__)     # inner
print(holiday.__doc__)     # 这个是inner函数