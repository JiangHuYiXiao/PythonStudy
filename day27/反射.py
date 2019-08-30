#-*- coding:utf-8 -*-
# 反射：就是通过字符串形式去操作类或者对象属性的相关属性。

# V1
# class Teacher:
#     dic = {'查看学生信息':'','查看老师信息':''}
#
#     def search_student(self):
#         print('show_student')
#     def search_teacher(self):
#         print('show_teacher')
#
#     @classmethod
#     def func1(cls):
#         print('类方法使用一般使用类调用')
#     @staticmethod
#     def func2():
#         print('静态方法使用一般使用类调用')
#
# # 1、通过字符串去操作静态属性和类方法、静态方法
# # 静态属性
# #     方法1：通过循环
# menu = Teacher.dic
# for i in menu:
#     print(i)
#     #方法2：通过反射
# ret = getattr(Teacher,'dic')
# print(ret)
# # 类方法
# ret2 = getattr(Teacher,'func1')
# ret2()
#
# # 静态方法
# ret3 = getattr(Teacher,'func2')
# ret3()
#
# # # 没有该字符串则报错
# ret4 = getattr(Teacher,'fu')
# print(ret4)


# V2: 使用getattr和hasattr搭配使用  hasattr判断是否存在则运行，不存在则不运行
# class Teahcer:
#     dic = {'查看学生信息':'','查看老师信息':''}
#
#     def search_student(self):
#         print('show_student')
#     def search_teacher(self):
#         print('show_teacher')
#
#     @classmethod
#     def func1(cls):
#         print('类方法使用一般使用类调用')
#     @staticmethod
#     def func2():
#         print('静态方法使用一般使用类调用')
#
# # # 1、通过字符串去操作静态属性和类方法、静态方法-----类  不使用反射时一定可以通过“类名.变量名调用”
# # 静态属性
# if hasattr(Teahcer,'dic'):          # 如果存在dic字符串则运行下面的，不存在则不运行，不会报错
#     ret = getattr(Teahcer,'dic')
#     print(ret)
# # 类方法
# if hasattr(Teahcer,'func1'):
#     ret2 = getattr(Teahcer,'func1')
#     ret2()
#
# # 静态方法
# if hasattr(Teahcer,'func2'):
#     ret3 = getattr(Teahcer,'func2')
#     ret3()
#
# 2、使用字符串去操作静态属性、类的属性、类方法、静态方法----对象
# class Teahcer:
#     dic = {'查看学生信息':'','查看老师信息':''}
#
#     def search_student(self):
#         print('show_student')
#     def search_teacher(self):
#         print('show_teacher')
#
#     @classmethod
#     def func1(cls):
#         print('类方法使用一般使用类调用')
#     @staticmethod
#     def func2():
#         print('静态方法使用一般使用类调用')
#
# # 静态属性
# jianghu = Teahcer()
# if hasattr(jianghu,'dic'):          # 如果存在dic字符串则运行下面的，不存在则不运行，不会报错
#     ret = getattr(jianghu,'dic')
#     print(ret)
# # 类方法
# if hasattr(jianghu,'func1'):
#     ret2 = getattr(jianghu,'func1')
#     ret2()
#
# # 静态方法
# if hasattr(jianghu,'func2'):
#     ret3 = getattr(jianghu,'func2')
#     ret3()

# # 3、实际应用
# class Teahcer:
#     dic = {'查看学生信息':'search_student','查看老师信息':'search_teacher'}         # 字典的value和方法名一样
#
#     def search_student(self):
#         print('show_student')
#     def search_teacher(self):
#         print('show_teacher')
# jianghu = Teahcer()
# for i in Teahcer.dic:
#     print(i)
# req = input('请输入需求：')       # 字符串
# if hasattr(jianghu,Teahcer.dic[req]):   # 字符串
#     ret = getattr(jianghu,Teahcer.dic[req])
#     ret()


# 这样我们就可以依据用户输入的需求，去进入不同的菜单，执行不同的功能

# 4、反射模块(自定义和内置)的属性
# import my
# print(my.day)
#
#     # 4.1 使用反射的形式获取模块中的属性
# res = getattr(my,'day')
# print(res)
#
#     # 4.2 使用反射的形式获取模块中的方法
# res1 = getattr(my,'wahaha')
# res1()
#
# # 5、反射自己模块中的方法和属性 ---经常使用
# import sys
# print(sys.modules)
# age = 18
# def qqxing():
#     print('qqqqqq')
# # 属性
# res3 = getattr(sys.modules['__main__'],'age')
# print(res3)
#
# # 方法
# res2 = getattr(sys.modules['__main__'],'qqxing')
# res2()
#
# # 使用情况
# 变量名 = input('>>>')
# result = getattr(sys.modules['__main__'],变量名)
# print(result)
# #>>>age
# # 18
# # 以后再用反射取自己模块的内容时，使用：
# 变量名 = input('>>>')
# result = getattr(sys.modules[__name__],变量名)
# print(result)

# 6、要反射的函数有参数 getattr(模块名,'反射的变量名'(参数))
# import time
# # print(time.strftime('%Y-%m-%d %H:%M:%S'))
# print(getattr(time,'strftime')('%Y-%m-%d %H:%M:%S'))

# 7、一个模块中的类也能通过反射得到
import my
print(getattr(my,'C'))
print(getattr(my,'C')(12)) # 实例化

# 8、一般情况下hasattr和getattr联合使用的,这样提前判断下，就不会因为不存在而报错
if hasattr(my,'year'):
    print(getattr(my,'year'))

# 9、setarttr   设置修改变量
class A:
    pass
a = A()
setattr(A,'name','sb')          # 添加类属性
setattr(a,'name','alex')          # 添加对象属性
print(A.name)
print(a.name)

# 10、删除
delattr(a,'name')   # 删除对象的则用类的，
print(a.name)

delattr(A,'name')   # 报错，删除类的，如果还调用
print(a.name)
