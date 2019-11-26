#-*- coding:utf-8 -*-

#练习1：人狗大战
'''
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
'''
# 练习2：在终端输出如下信息

# 小明，10岁，男，上山去砍柴
# 小明，10岁，男，开车去东北
# 小明，10岁，男，最爱大保健
# 老李，90岁，男，上山去砍柴
# 老李，90岁，男，开车去东北
# 老李，90岁，男，最爱大保健
# 老张…
class Person:               # 一类作为类
    def __init__(self,*args):
        self.name = args[0]         # 特征作为属性
        self.age = args[1]
        self.sex = args[2]
    def moutain(self):              # 动作一般作为方法
        print('%s,%s岁,%s,上山去砍柴'%(self.name,self.age,self.sex))
    def drive(self):
        print('%s,%s岁，%s，开车去东北'%(self.name,self.age,self.sex))
    def enjoy(self):
        print('%s,%s岁,%s,最爱大保健'%(self.name,self.age,self.sex))
ming = Person('小明',10,'男')
ming.moutain()
ming.drive()
ming.enjoy()

li = Person('老李',90,'男')
li.moutain()
li.drive()
li.enjoy()

# 使用面向对象的场景
# 1、当有几个函数反复使用相同的参数时，可以考虑面向对象，这些参数就是属性。
# 2、非常明显的处理一类事物，这些事物具有相似的属性和功能时。

# 练习3：计算圆周长和面积
from math import pi
class Circle:
    def __init__(self,*args):
        self.r = args[0]
    def cir(self):
        print('圆的周长为:%s'%(2*pi*self.r))
    def area(self):
        print('圆的面积为:%s'%(pi*self.r**2))
C1 = Circle(3)
C1.cir()
C1.area()



