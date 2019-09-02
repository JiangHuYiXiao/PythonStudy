# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/8/31 7:46
# @Software       : PyCharm
# @Python_verison : 3.7

# 双下类的内置方法
# 1、__str__
# 之前我们学过repr()方法是返回真实的数据类型
print(repr('1'))            # '1'
print(str('1'))             # 1
# 我们之前学的len(),内部也是调用的双下__len__()
# 内置的类方法__len__()和内置的方法是存在关系的，我们继续往下学习

# 验证使用str方法时用的是类中的双下__str__()方法
class A:
    # def __str__(self):
    #     return 'A'
    pass

a = A()
print(str(a))           # 注释结果：<__main__.A object at 0x00000000027B3EF0>  不注释结果：A
# 结论：
# str()实际用的是双下__str__()方法，当子类自己有__str__()方法时用子类自己的，没有就用父类的，
# 或者object类的，由于object中有默认的一个双下str方法，默认返回这个调用方法的对象的内存地址
#     def __str__(self, *args, **kwargs): # real signature unknown
#         """ Return str(self). """
#         pass
# 所以始终能够使用双下str方法

# 像list他是重新写了str方法,所以他不打印出内存地址
list = [1,2,3]
print(list)

# %s，str(),print(),实际上走得都是双下str

# 自己重写str方法是有很大用处的，举例如下：
class Teacher:
    def __init__(self,name,salary):
        self.name = name
        self.salary =salary
    def __str__(self):
        return ("Teacher's object:%s"%(self.name))   # 重写了返回这个，不重写返回内存地址,重写时必须返回str数据类型
    def func(self):
        print('wahaha')

liu = Teacher('刘老师',20000)
print(liu)

# 2、__repr__
class Teacher:
    def __init__(self,name,salary):
        self.name = name
        self.salary =salary
    def __str__(self):
        return ("Teacher's object:%s"%(self.name))   # 重写了返回这个，不重写返回内存地址，重写时必须返回str数据类型
    def __repr__(self):
        return str(self.__dict__)   # 重写时必须返回str数据类型
    def func(self):
        print('wahaha')

liu = Teacher('刘老师',20000)
print(liu)               # Teacher's object:刘老师
print('%s'%liu)         # Teacher's object:刘老师
print(str(liu))         # Teacher's object:刘老师

print('%r'%liu)         # {'name': '刘老师', 'salary': 20000}
print(repr(liu))        # {'name': '刘老师', 'salary': 20000}
# %r 和repr()都是走得__repr__



# 3、双下__repr__和双下__str__的顺序：
# 使用（str()，print，%s）有__str__时先用__str__，没有就用__repr__，
# 使用（repr()，%r）只能用__repr__，
class Teacher:
    def __init__(self,name,salary):
        self.name = name
        self.salary =salary
    # def __str__(self):
    #     return ("Teacher's object:%s"%(self.name))   # 重写了返回这个，不重写返回内存地址，重写时必须返回str数据类型
    def __repr__(self):
        return str(self.__dict__)   # 重写时必须返回str数据类型
    def func(self):
        print('wahaha')

liu = Teacher('刘老师',20000)
print(liu)               # {'name': '刘老师', 'salary': 20000}
print('%s'%liu)         # {'name': '刘老师', 'salary': 20000}
print(str(liu))         # {'name': '刘老师', 'salary': 20000}

print('%r'%liu)         # {'name': '刘老师', 'salary': 20000}
print(repr(liu))        # {'name': '刘老师', 'salary': 20000}


class Teacher:
    def __init__(self,name,salary):
        self.name = name
        self.salary =salary
    def __str__(self):
        return ("Teacher's object:%s"%(self.name))   # 重写了返回这个，不重写返回内存地址，重写时必须返回str数据类型
    # def __repr__(self):
    #     return str(self.__dict__)   # 重写时必须返回str数据类型
    def func(self):
        print('wahaha')

liu = Teacher('刘老师',20000)
print(liu)               # {'name': '刘老师', 'salary': 20000}
print('%s'%liu)         # {'name': '刘老师', 'salary': 20000}
print(str(liu))         # {'name': '刘老师', 'salary': 20000}

print('%r'%liu)         # <__main__.Teacher object at 0x00000000023022B0>
print(repr(liu))        # <__main__.Teacher object at 0x00000000023022B0>
# 如果在程序中，只能实现一个就实现__repr__这样，str也可以用



# 4、内置的方法很多，不一定全部在object中，比如我们的len方法
class A:
    # def __len__(self):
        # return 10
    pass

a = A()
print(len(a))           # TypeError: object of type 'A' has no len() 提示object中没有len方法

# 5、__len__的实际应用
class Classes:
    def __init__(self,name):
        self.name = name
        self.student = []
    def __len__(self):
        return len(self.student)

py9 = Classes('py9')
py9.student.append('老二')
py9.student.append('老大')

print(len(py9))


# 6、__del__
class A:
    def __del__(self):  # 析构函数，删除一个对象之前先做收尾工作
        print('执行我啦！')
a = A()
del a           # 即执行这个__del__方法，又删除了变量
print(a)

# 7、__call__  等价于 对象（）
class A:
    def __init__(self,name):
        pass
    def __call__(self):  #
        print('执行我啦！')
        '''
        比如打印对象中的所有属性
        '''
        for k in self.__dict__:
            print(k,self.__dict__[k])


a = A('alex')()   # == 对象()就相当于执行了__call__
