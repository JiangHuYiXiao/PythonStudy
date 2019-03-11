# -*- coding:utf-8 -*-
'''
# 导入pi
from math import pi
# 定义一个圆类
class Circle:
    def __init__(self,r):
        self.r = r
    def cir(self):
        return (2*pi*self.r)
    def area(self):
        return (pi*self.r**2)
# 定义一个圆实例（对象）
C1 = Circle(2)
print(C1.cir())
print(C1.area())

# 练习1：计算一个圆环的面积和周长
class Ring:
    def __init__(self,outside_r,inside_r):
        # 一个类的对象Circle(outside_r)作为另一个类的属性self.outside_c
        self.outside_c = Circle(outside_r)
        self.inside_c = Circle(inside_r)
    def area(self):
        return self.outside_c.area() - self.inside_c.area()
    def cir(self):
        return self.outside_c.cir() + self.inside_c.cir()

r1= Ring(20,10)
print(r1.area())
print(r1.cir())
'''
# 练习2 ：创建一个老师类，老师有生日，生日可以作为一个类，利用组合的方式去做
class Teacher:
    def __init__(self,name,birthday,sex):
        self.sex = sex
        self.name = name
        self.birthday = birthday
        self.course = Course('python',6,2000)


class Birthday:
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day

class Course:
    language = 'chinese'

    def __init__(self, *args):
        self.teacher = args[0]
        self.period = args[1]
        self.price = args[2]

    def func(self):
        print('%s个月学结束' % (self.period))

B1 = Birthday(2019,1,3)
T1 = Teacher('jiangxi',B1,'man')
print(T1.name)
print(T1.birthday)
# 生日组合
print(T1.birthday.year)
print(T1.birthday.month)
# 课程组合
print(T1.course.price)
print(T1.course.period)
