# -*- coding:utf-8 -*-
# 1、定义类：
# class 类名:
#     pass

class Person:                       # Person就是一个类  ,类的名字，首字母大写
    country = 'china'                   # 静态属性

    def __init__(self,*args):           # 通过__init__() 初始化方法可以往self里面放值，且返回一个self对象
        # print(self.__dict__)
        self.name = args[0]         # self实质也是一个对象,name、hp、aggr、sex就是属性
        self.hp = args[1]
        self.aggr = args[2]
        self.sex = args[3]
        # print(self.__dict__)      # 调用所有属性
        # print(id(self))           # 32532912,判断出self和alex是同一个内存地址
    def walk(self,n):               # 函数放类里面一般叫做方法
        print('%s:Let go!,走了%s步'%(self.name,n))

# alex = Person('alex',100,10,'man')          # 实例化，alex是个对象,本质是self
# print(alex)                   # <__main__.Person object at 0x0000000002286470>
# print(alex.__dict__)          # 查看调用所有属性
# print(alex.name)              # 查看单个属性调用
# print(id(alex))         # 32532912,判断出self和alex是同一个内存地址

# 2、实例化
# 实例 = 类名(参数)
alex = Person('alex',100,10,'man')

# 实例化过程：
    # 1、类名（参数）首先会创建一个self对象，
    # 2、默认就会调用__init__(参数)方法，接收参数
    # 3、执行__init__(参数)方法，返回self


# 3、类的作用：
    # 1、调用方法格式:   类名.方法名(self,参数)
Person.walk(alex,2)
    # 2、调用属性：一般是调用公共属性，也就是静态属性  对象.属性
print(Person.country)           # china
# Person.name                   # AttributeError: type object 'Person' has no attribute 'name',不能调用对象的属性


# 4、对象的作用
    # 1、调用属性：对象属性、静态属性，对象.属性
print(alex.name)            # alex
print(alex.country)         # china
    # 2、调用方法：对象.方法(参数)
alex.walk(2)

# 5、类和对象都可以调用__dict__方法，通过使用__dict__方法操作属性
print(Person.__dict__)          # 返回所有的属性值
print(alex.__dict__)            # 返回对象的所有属性值

# 查看
print(Person.__dict__['country'])
print(alex.__dict__['name'])


# 对象可以调用__dict__方法来操作对象的属性，进行增删改查
# 修改
alex.__dict__['name'] = '老二'
print(alex.name)
# Person.__dict__['country'] = 'USA'  类的属性不通过__dict__ 修改，只能查看


# 一般建议这么修改对象、类的属性
alex.name = '大师兄'
print(alex.__dict__)            # {'name': '大师兄', 'hp': 100, 'aggr': 10, 'sex': 'man'}
Person.country = 'USA'
print(Person.__dict__)
print(alex.country)             # USA




