#-*- coding:utf-8 -*-
# 反射：就是通过字符串形式去操作类或者对象属性的相关属性。
'''
# V1
class Teahcer:
    dic = {'查看学生信息':'','查看老师信息':''}

    def search_student(self):
        print('show_student')
    def search_teacher(self):
        print('show_teacher')

    @classmethod
    def func1(cls):
        print('类方法使用一般使用类调用')
    @staticmethod
    def func2():
        print('静态方法使用一般使用类调用')

# 1、通过字符串去操作静态属性和类方法、静态方法
# 静态属性
    # 方法1：通过循环
# menu = Teahcer.dic
# for i in menu:
#     print(i)
    #方法2：通过反射
ret = getattr(Teahcer,'dic')
print(ret)
# 类方法
ret2 = getattr(Teahcer,'func1')
ret2()

# 静态方法
ret3 = getattr(Teahcer,'func2')
ret3()

# 没有改字符串则报错
ret4 = getattr(Teacher,'fu')
print(ret4)


# V2: 使用getattr和hasattr搭配使用
class Teahcer:
    dic = {'查看学生信息':'','查看老师信息':''}

    def search_student(self):
        print('show_student')
    def search_teacher(self):
        print('show_teacher')

    @classmethod
    def func1(cls):
        print('类方法使用一般使用类调用')
    @staticmethod
    def func2():
        print('静态方法使用一般使用类调用')

# 1、通过字符串去操作静态属性和类方法、静态方法-----类
if hasattr(Teahcer,'dic'):          # 如果存在dic字符串则运行下面的，不存在则不运行，不会报错
    ret = getattr(Teahcer,'dic')
    print(ret)
# 类方法
if hasattr(Teahcer,'func'):
    ret2 = getattr(Teahcer,'func')
    ret2()

# 静态方法
if hasattr(Teahcer,'func2'):
    ret3 = getattr(Teahcer,'func2')
    ret3()

# 2、使用字符串去操作静态属性、类的属性、类方法、静态方法----对象
class Teahcer:
    dic = {'查看学生信息':'','查看老师信息':''}

    def search_student(self):
        print('show_student')
    def search_teacher(self):
        print('show_teacher')

    @classmethod
    def func1(cls):
        print('类方法使用一般使用类调用')
    @staticmethod
    def func2():
        print('静态方法使用一般使用类调用')
jianghu = Teahcer()
if hasattr(jianghu,'dic'):          # 如果存在dic字符串则运行下面的，不存在则不运行，不会报错
    ret = getattr(jianghu,'dic')
    print(ret)
# 类方法
if hasattr(jianghu,'func1'):
    ret2 = getattr(jianghu,'func1')
    ret2()

# 静态方法
if hasattr(jianghu,'func2'):
    ret3 = getattr(jianghu,'func2')
    ret3()
'''
# 3、实际应用
class Teahcer:
    dic = {'查看学生信息':'search_student','查看老师信息':'search_teacher'}         # 字典的value和方法名一样

    def search_student(self):
        print('show_student')
    def search_teacher(self):
        print('show_teacher')
jianghu = Teahcer()
for i in Teahcer.dic:
    print(i)
req = input('请输入需求：')       # 字符串
if hasattr(jianghu,Teahcer.dic[req]):   # 字符串
    ret = getattr(jianghu,Teahcer.dic[req])
    ret()


# 这样我们就可以依据用户输入的需求，去进入不同的菜单，执行不同的功能