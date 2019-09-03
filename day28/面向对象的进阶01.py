# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/9/3 8:23
# @Software       : PythonStudy
# @Python_verison : 3.7
'''

# item系列  ：操作对象跟操作字典类似，或者列表索引一样
# 1、__getitem__,获取属性值
class Teacher:
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
    def __getitem__(self, item):
        if hasattr(self,item):
            return self.__dict__[item]

T1 = Teacher('py',21,'男')
print(T1.__dict__)      # 通过对象查询所有属性 {'name': 'py', 'age': 21, 'sex': '男'}
print(T1.name)          # 通过对象查询某个属性 py
print(T1['name'])           # 通过getitem，键值对的方式查询
print(T1['age'])           # 通过getitem，键值对的方式查询


# 2、__setitem__,设置属性值
class Teacher:
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
    def __getitem__(self, item):
        if hasattr(self,item):
            return self.__dict__[item]
    def __setitem__(self, key, value):
        self.__dict__[key] = value

T1 = Teacher('py',21,'男')
# print(T1.__dict__)      # 通过对象查询所有属性 {'name': 'py', 'age': 21, 'sex': '男'}
# print(T1.name)          # 通过对象查询某个属性 py
# print(T1['name'])           # 通过getitem，键值对的方式查询
# print(T1['age'])           # 通过getitem，键值对的方式查询

T1['hobby'] = '男'       # 通过setitem进行赋值
print(T1.hobby)
print(T1['hobby'])         # 通过getitem进行查询


# 3、delitem  删除属性
class Teacher:
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
    def __getitem__(self, item):
        if hasattr(self,item):
            return self.__dict__[item]
    def __setitem__(self, key, value):
        self.__dict__[key] = value
    def __delitem__(self, key):
        del self.__dict__[key]

T1 = Teacher('py',21,'男')
# print(T1.__dict__)      # 通过对象查询所有属性 {'name': 'py', 'age': 21, 'sex': '男'}
# print(T1.name)          # 通过对象查询某个属性 py
# print(T1['name'])           # 通过getitem，键值对的方式查询
# print(T1['age'])           # 通过getitem，键值对的方式查询

T1['hobby'] = '男'       # 通过setitem进行赋值
print(T1.hobby)
print(T1['hobby'])         # 通过getitem进行查询
del T1['hobby']         # 通过delitem进行删除
print(T1.__dict__)


# 4、__new__   创建对象，最优先 ，如果重写了new方法那么用的都是同一个对象，否则的每次用的是不同的对象
class A:
    def __init__(self):                                  # 第4步
        self.x = 1                                       # 第5步
        print('in init function')                      # 第6步
    def __new__(cls, *args, **kwargs):                   # 第3步
        print('in new function')                       # 第2步
        return object.__new__(A, *args, **kwargs)        # 第3步

a = A()

# in new function
# in init function

# 著名的设计模式1，单例设计模式
# 一个类始终只有一个对象
# new的应用
class A:
    __instance = False
    def __init__(self,name):
        self.name = name
    def __new__(cls, *args, **kwargs):
        if cls.__instance:
            return cls.__instance
        else:
            cls.__instance = object.__new__(cls)
            return cls.__instance

a1 = A('egon')
a2 = A('son')
print(a1)           # <__main__.A object at 0x0000000001F05780>

print(a2)           # <__main__.A object at 0x0000000001F05780>

print(a1.name)          # son
print(a2.name)          # son  证明了每次都是用的同一个对象，单实例

# 5、__eq__  判断两个对象是否相等时，可以重写，如果不重写则两个对象不相等
class A:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    # def __eq__(self, other):
    #     if self.__dict__ == other.__dict__:
    #         return True
    #     else:
    #         return False

egon = A('alex',21)
alex = A('alex',21)
print(egon == alex)    # 不实现eq则是false，不是先默认比较的是内存地址，实现则是True，走得是eq方法
'''
# 6、hash方法，当对象的属性值一致时，如果重写了__hash__方法那么结果一致
class A:
    def __init__(self,name,sex):
        self.name = name
        self.sex = sex
    def __hash__(self):
        return hash(self.name+self.sex)

# 没有重写
A1 = A('jianghu','男')
A2 = A('jiangxi','男')
print(hash(A1))         # -8290069429123698291
print(hash(A2))         # 6446190177644587080

# 重写了__hash__()方法
A1 = A('jianghu','男')
A2 = A('jianghu','男')
print(hash(A1))         # 4771437910318130738
print(hash(A2))         # 4771437910318130738