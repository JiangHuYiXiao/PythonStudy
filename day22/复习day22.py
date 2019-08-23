# 练习1：人狗大战

# 人类
'''


class Person:
    def __init__(self,name,blood,aggr,sex):
        self.name = name
        self.blood = blood
        self.sex = sex
        self.aggr = aggr
    # 人打的方法
    def person_attack(self,dog):
        dog.blood = dog.blood - self.aggr
        print('%s被%s打了，掉了%s血，剩下%s血'%(dog.name,self.name,self.aggr,dog.blood))

# 狗类
class Dog:
    def __init__(self,name,blood,aggr,sex):
        self.name = name
        self.blood = blood
        self.aggr = aggr
        self.sex = sex
    # 狗攻击的方法
    def dog_attack(self,person):
        person.blood = person.blood - self.aggr
        print('%s被%s咬了，掉了%s血,剩下%s血'%(person.name,self.name,self.aggr,person.blood))

P1 = Person('江湖',100,10,'女')
D1 = Dog('teedy',80,20,'女')
P1.person_attack(D1)
D1.dog_attack(P1)

# 练习2：在终端输出如下信息

# 小明，10岁，男，上山去砍柴
# 小明，10岁，男，开车去东北
# 小明，10岁，男，最爱大保健
# 老李，90岁，男，上山去砍柴
# 老李，90岁，男，开车去东北
# 老李，90岁，男，最爱大保健
# 老张…

class Person:
    def __init__(self,age,name,sex):
        self.age  = age
        self.name = name
        self.sex = sex

    #  砍柴的方法
    def moutain(self):
        print('%s,%s,%s,上山去砍柴'%(self.name,self.age,self.sex))

    # 开车的方法
    def driver(self):
        print('%s,%s,%s,开车去东北'%(self.name,self.age,self.sex))

    # enjoy的方法
    def enjoy(self):
        print('%s,%s,%s,最爱大保健'%(self.name,self.age,self.sex))

P1 = Person('小明',10,'男')
P1.moutain()
P1.driver()
P1.enjoy()

P1 = Person('老李',90,'男')
P1.moutain()
P1.driver()
P1.enjoy()
'''

# 练习3：计算圆周长和面积
from math import pi
class Round:
    def __init__(self,r):
        self.r = r
    # 周长的方法
    def perimeter(self):
        return 2*pi*self.r

#     面积的方法
    def area(self):
        return pi*self.r**2

R1 = Round(3)
print(R1.perimeter())
print(R1.area())
