#-*- coding:utf-8 -*-
# 面向对象的三大特性
#     1、继承
#     2、多态
#     3、封装

# 1、一个子类继承一个父类
class A:
    pass

class A_son(A):         # 表示A_son继承A,A称作为父类（超类、基类），A_son是子类（派生类）
    pass

# 2、一个子类继承多个父类      只有python特有，其他语言没有
class A:
    pass
class B:
    pass
class A_son1(A,B):         # 表示A_son1继承A\B,A\B称作为父类（超类、基类），A_son1是子类（派生类）
    pass

# 3、一个父类被多个子类继承
class A:
    pass
class B_son(B):
    pass
class A_son2(A):         # 表示A_son2\B_son继承A,A称作为父类（超类、基类），A_son1\B_son是子类（派生类）
    pass

# 结论：子类可以找到父类，但是父类不知道自己的子类，各个子类之间没有关系

# 4、查看子类继承的是哪个父类
print(A_son.__bases__)          # (<class '__main__.A'>,)
print(B_son.__bases__)          # (<class '__main__.B'>,)

# 5、在python中所有的类都有父类，因为他们如果没有继承父类，默认继承object类
print(B.__bases__)              # (<class 'object'>,),所有类的最终父类都是object类

# 6、抽象与继承
# 抽象是把事物类似的那一部分抽取出来
# 抽象分为两个层次：
#    1、将奥巴马和梅西抽取出来就是一个人类。
#    2、将人、狗、猪抽取出来就是一个动物父类。（继承）
#    3、继承是表示什么是什么的关系（人是动物）
# 继承是基于抽象的结果，通过编程语言去实现他，看到要经历抽象这个过程，才能通过继承的方式表达抽象的结构


# 把人狗类的相同部分抽象出来成为一个父类
'''
class Animal:
    def __init__(self,name,aggr,hp):
        self.name = name
        self.aggr = aggr
        self.hp = hp


class Dog(Animal):
    def bite(self,person):
        person.hp = person.hp - self.aggr

class Person(Animal):
    def attack(self,dog):
        dog.hp = dog.hp - self.aggr

xiaohei = Dog('xiaohei',100,200)
print(xiaohei.name)
jianghu = Person('jianghu',10,1000)
print(jianghu.aggr)
'''

# 面试题：
class Animal:
    def __init__(self):         # 2、执行init方法
        print('执行Animal.__init__')          # 3、输出
        self.func()         # 4、dog调用函数，因为Dog有所以调用的是Dog的
    def eat(self):
        print('%s eating'%(self.name))
    def drink(self):
        print('%s drink'%(self.name))
    def func(self):
        print('Animal func')

class Dog(Animal):
    def guard(self):
        print('guarding')
    def func(self):         # 5、输出
        print('Dog Animal')

dog = Dog()   # 1、首先创建self对象，其实就是dog
# 执行Animal.__init__
# Dog Animal
