# -*- coding:utf-8 -*-
'''
class Animal:
    def __init__(self,name,aggr,hp):
        self.name = name
        self.aggr = aggr
        self.hp = hp
    def eat(self):     # 人和狗都可以继承该方法
        print('吃东西')
        self.hp = self.hp + 100


class Dog(Animal):
    def __init__(self,name,aggr,hp,kind):
        #需要使用父类的init方法，使用name,aggr,hp三个属性
        Animal.__init__(self,name,aggr,hp)              # # self也需要传，这个类的所有self都是狗的对象
        self.kind = kind                # 派生属性
    def bite(self,person):          # 派生方法
        person.hp = person.hp - self.aggr

class Person(Animal):
    def __init__(self,name,aggr,hp,sex):
        #需要使用父类的init方法，使用name,aggr,hp三个属性
        Animal.__init__(self,name,aggr,hp)              # self也需要传，这个类的所有self都是人的对象
        self.sex = sex          # 派生属性
        self.money = 0          # 派生属性
    def attack(self,dog):           # 派生方法
        dog.hp = dog.hp - self.aggr

xiaohei = Dog('xiaohei',100,200,'teddy')
print(xiaohei.name)
jianghu = Person('jianghu',10,1000,'man')
print(jianghu.aggr)
xiaohei.eat()
print(xiaohei.hp)
jianghu.eat()
print(jianghu.hp)
'''
# 结论：
#     1、父类中没有的属性在子类中有是派生属性
# #     2、父类中没有的方法在子类中有是派生方法
# #     3、只要是子类的对象调用，子类中有就用子类的，子类没有就用父类，
# #     4、如果还想用父类的就直接调用

# 继承父类后还有自己的方法或者属性
# 比如：
class Animal:
    def __init__(self,name,aggr,hp):
        self.name = name
        self.aggr = aggr
        self.hp = hp
    def eat(self):     # 人和狗都可以继承该方法
        print('吃东西')
        self.hp = self.hp + 100


class Dog(Animal):
    def __init__(self,name,aggr,hp,kind):
        #需要使用父类的init方法，使用name,aggr,hp三个属性
        Animal.__init__(self,name,aggr,hp)              # # self也需要传，这个类的所有self都是狗的对象
        self.kind = kind                # 派生属性
    def bite(self,person):          # 派生方法
        person.hp = person.hp - self.aggr
    def eat(self):
        Animal.eat(self)            # 不仅实现了父类的功能，还有子类自己的功能，要使用父类的必须自己传self
        self.tooth = 2

class Person(Animal):
    def __init__(self,name,aggr,hp,sex):
        #需要使用父类的init方法，使用name,aggr,hp三个属性
        Animal.__init__(self,name,aggr,hp)              # self也需要传，这个类的所有self都是人的对象
        self.sex = sex          # 派生属性
        self.money = 0          # 派生属性
    def attack(self,dog):           # 派生方法
        dog.hp = dog.hp - self.aggr


xiaohei = Dog('xiaohei',10,100,'teddy')
xiaohei.eat()
print(xiaohei.hp)
print(xiaohei.tooth)
