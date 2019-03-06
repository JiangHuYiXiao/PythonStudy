# -*- coding:utf-8 -*-
# 1、定义类，首字母大写
# 类中有一个默认的初始化方法__init__(self)
class Person:
# 2、初始化方法__init__()
# 5、定义静态属性
    country = 'china'
    def __init__(self,*args):           # self就是一个对象
#3、定义类的属性
        self.name = args[0]
        self.age = args[1]
# 4、定义方法，在类中叫做方法（也可称为动态属性），外部称为函数
    def study(self,info):
        print('%s:你已经%s岁了,%s'%(self.name,self.age,info))

# 6、实例化
# 对象 = 类名(*args)   实例就是对象
jianghu = Person('jianghu',10)

# 7、对象的使用
#   查看属性
print(jianghu.__dict__)
print(jianghu.name)
#   修改属性
jianghu.name = 'jiang'
jianghu.__dict__['name'] = 'jiangxi'
print(jianghu.name)
#  调用方法
jianghu.study('好好学习')

# 8、类的使用
#   查看静态属性
print(Person.country)
print(Person.__dict__)
#   修改属性
Person.country = 'usa'
print(Person.country)
Person.name =  'jiangjiang'
print(Person.name)
Person.__dict__['name'] = 'jianghuyixiao'           # TypeError: 'mappingproxy' object does not support item assignment
print(Person.country)
# 调用方法
Person.study(jianghu,'是大人了')


# 练习1：使用面向对象的思路，计算正方形的周长和面积
class Square:
    def __init__(self,*args):
        self.side = args[0]
    def circle(self):
        # print('正方形的周长为：%s'%(self.side*4))   一般不直接输出，尽量返回，可以对这个值继续操作
        return self.side*4
    def area(self):
        # print('正方形的面积为：%s'%(self.side*self.side))
        return self.side*self.side
Z1 = Square(2)
print(Z1.circle())
print(Z1.area())
