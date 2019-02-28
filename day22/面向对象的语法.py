# -*- coding:utf-8 -*-
# 1、定义类：
# class 类名:
#     pass

class Person:                       # Person就是一个类
    def __init__(self,*args):           # 通过__init__方法可以往self里面放值
        print(self.__dict__)
        self.name = args[0]         # self实质也是一个对象,name、hp、aggr、sex就是属性
        self.hp = args[1]
        self.aggr = args[2]
        self.sex = args[3]
        print(self.__dict__)
        print(id(self))         # 32532912
    def walk(self):
alex = Person('alex',100,10,'man')          # alex是个对象,本质是self
# print(alex)         # <__main__.Person object at 0x0000000002286470>
# print(alex.name)
# print(alex.hp)
# print(alex.sex)
print(id(alex))         # 32532912


# 2、实例化
# 实例 = 类名(参数)


# 类名（参数）得到一个self对象，也就是实例化，默认就会调用__init__方法，接收参数，返回self
# 2、Python中一切都是对象