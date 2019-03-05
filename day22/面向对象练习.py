#-*- coding:utf-8 -*-

#练习人狗大战

# 狗类
class Dog:
    def __init__(self,name,blood,attr,sex):
        self.name = name
        self.blood = blood
        self.attr = attr
        self.kind = sex
    def bite(self,person):
        person.blood = person.blood - self.attr
        print('%s被咬了，掉了%s血'%(person.name,self.attr))
teddy = Dog('teddy',100,1,'man')        # 实例化创建对象，teddy

#人类
class Person:
    def __init__(self,name,blood,attr,sex):
        self.name = name
        self.blood = blood
        self.attr = attr
        self.kind = sex
    def attack(self,dog):
        dog.blood = dog.blood - self.attr
        print('%s被打了，掉了%s血'%(dog.name,self.attr))
rose = Person('rose',1000,10,'man')         # 实例化创建对象，Rose

# 人打狗
rose.attack(teddy)
print(teddy.blood)

# 狗咬人
teddy.bite(rose)
print(rose.blood)


