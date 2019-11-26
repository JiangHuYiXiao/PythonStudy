# -*- coding:utf-8 -*-
# 1、列表解析---等价于列表推导式
egg_list = ['egg%s'%i for i in range(10)]
print(egg_list)             # ['egg0', 'egg1', 'egg2', 'egg3', 'egg4', 'egg5', 'egg6', 'egg7', 'egg8', 'egg9']


# 2、把列表符号[]改成（）就是一个生成器表达式
egg_list = ('egg%s'%i for i in range(10))
print(egg_list)             # <generator object <genexpr> at 0x0000000001F33750>

# 对生成器进去取值

# 方法2：
for i in egg_list:
    print(i)

# 方法2：
# 列表推导式和生成器表达式，是一种代码编写的简易方式，两者都可以实现相同的功能，但是生成器表达式更加节省内存