# -*- coding:utf-8 -*-
# 内置函数分类：
# 一、作用域相关
# 1、globals() 一定返回全局作用域的所有变量
# 2、locals() 如果在全局则返回全局作用域的所有变量，如果在局部则返回局部作用域的所有变量
# a = 10
# def func(*args,**kwargs):
#     b = 20
#     print('***',b)
#     print(locals())         # 返回局部作用域的的所有变量
#
# print(globals())            # 返回全局作用域的所有变量
# func()


# 二、其他
# 1、输入输出
# 输入input()

# res = input('请输入：')
# print(res)

# 输出print()   def print(self, *args, sep=' ', end='\n', file=None):
# end 指定输出的结束符
# print('江湖一笑\n') # 默认会换行end='\n',可以自己定义end值
# print('江湖一笑',end='')
# print('江湖一笑',end='888888')   # 江湖一笑江湖一笑
# print('江湖一笑')   # 江湖一笑江湖一笑888888江湖一笑

# sep指定多个不同元素的连接符
# print('江湖一笑','jianghuyixiao',sep='==')   #江湖一笑==jianghuyixiao

# file,默认输出到屏幕，但是可以自己修改到指定文件
# f = open('file',mode='w+',encoding='utf-8')
# print('woqu',file=f)            # 输出到指定文件file里面去了
# f.close()

# 2、查看（变量、函数）对象的内置属性名
# dir()
# print(dir([]))
# print(dir(2))

# 3、帮助
# help()  比dir（）更详细，dir（）给出的是方法名
help(list)
