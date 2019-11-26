# -*- coding:utf-8 -*-、
# 组合表示的是什么有什么的关系
# 一个类的属性值是另一个类的对象时，调用的时候：用对象.属性.属性
# 人狗大战优化版
    # 人类
class Person:
    country = 'china'
    def __init__(self,name,aggr,hp,sex):
        self.name = name
        self.aggr = aggr
        self.hp = hp
        self.sex = sex
        self.money = 0
    def attack(self,dog):           # 攻击
        dog_res = '%s狗被%s打了，掉了%s血，剩下%s血'%(dog.name,self.name,self.aggr,dog.hp - self.aggr)
        return(dog_res)
    def get_weapon(self,w):            # 捡武器
        if self.money >= w.price:
            self.money -= w.price
            self.weapon = w
            self.aggr += w.aggr
        else:
            print('余额不足，请及时充值')
alex = Person('alex',1,110,'man')

    # 狗类
class Dog:
    def __init__(self,name,aggr,hp,kind):
        self.name = name
        self.aggr = aggr
        self.hp = hp
        self.kind = kind
    def bite(self,person):          # 咬
        person_res = '%s人被%s咬了，掉了%s血，剩下%s血'%(person.name,self.name,self.aggr,person.hp - self.aggr)
        return person_res
frank = Dog('frank',100,200,'teddy')


    # 武器类，给人装备
class Weapon:
    def __init__(self,name,aggr,time,price):
        self.name = name
        self.aggr = aggr
        self.time = time
        self.price = price
    def master_stroke(self,person):     # 大招
        person.hp -= self.aggr*2
w = Weapon('打狗棒',10,20,900)
# 功能
    # 人打狗
print(alex.attack(frank))

    # 狗咬人
print(frank.bite(alex))
# 给alex钱
alex.money = 1000
# alex捡武器
alex.get_weapon(w)
print(alex.weapon)
# alex用武器打狗
alex.weapon.master_stroke(frank)
print(alex.hp)
print(frank.hp)