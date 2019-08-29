# -*- coding:utf-8 -*-
# @property 内置装饰器函数，只在面向对象中使用

'''
class Circle:
    def __init__(self,r):
        self.r = r

    def perimeter(self):
        return 2*pi*self.r

    def area(self):
        return  pi*self.r**2


C1 = Circle(2)
print(C1.area())
print(C1.perimeter())

# 我们的面积，周长应该是圆的属性
# 我们可以在方法前面加上@property把这个方法伪装为一个属性

from math import pi
class Circle:
    def __init__(self,r):
        self.r = r
    @property
    def perimeter(self):            # 这个伪装的属性不能传任何参数
        return 2*pi*self.r
    @property
    def area(self):                 # 这个伪装的属性不能传任何参数
        return  pi*self.r**2


C1 = Circle(2)
print(C1.area)              # 伪装后，直接用对象调用方法名
print(C1.perimeter)         # 伪装后，直接用对象调用方法名
'''
# 练习：
# BMI指数（bmi是计算而来的，但很明显它听起来像是一个属性而非方法，如果我们将其做成一个属性，更便于理解）

# 成人的BMI数值：
# 过轻：低于18.5
# 正常：18.5-23.9
# 过重：24-27
# 肥胖：28-32
# 非常肥胖, 高于32
# 　　体质指数（BMI）=体重（kg）÷身高^2（m）
# 　　EX：70kg÷（1.75×1.75）=22.86
# class Person:
#     def __init__(self,name,weight,high):
#         self.name = name
#         self.weight = weight
#         self.high = high
#     @property
#     def BMI(self):
#         return  self.weight/self.high**2
# p1 = Person('jianghu',65,1.7)
# print(p1.BMI)
# # p1.BMI = 11         # AttributeError: can't set attribute,这个伪装的属性不能修改，这样做就起到了保护的作用

# 修改方法作为伪装属性的值
class Person:
    def __init__(self,name):
        self.__name = name       # 私有属性
    @property
    def name(self):             # 方法伪装为属性，这样是为了保护这个属性不被随意修改，但是可以通过一定方式进行修改
        return  self.__name + 'sb'
    @name.setter                # 前面的name就是我们的方法名name
    def name(self,new_name):             # 再定义一个name方法
        self.__name = new_name

p1 = Person('hunan')
print(p1.name)
p1.name = 'hebei'
print(p1.name)
'''

# 练习2：超市促销活动,计算各个商品打折后的价格,前三天是5折，后面是8折
# 方法1：

class Goods:
    discount = 0.5
    def __init__(self,name,weight,price):
        self.name = name
        self.weight = weight
        self.price = price

apple = Goods('apple',2,5)
print(apple.price*apple.weight*apple.discount)


# 方法2
class Goods:
    discount = 0.5
    def __init__(self,name,weight,price):
        self.name = name
        self.weight = weight
        self.__price = price
    @property
    def price(self):
        return self.__price*self.discount*self.weight

apple_price = Goods('apple',3,6)
print(apple_price.price)
# 后面三天就只需要修改discount为0.8就可以
# 总结：@property一般是和私有属性一起使用，为了就是计算私有属性值，返回

# 通过@property对属性的增、删除、改、查

class Person:
    def __init__(self,name):
        self.__name = name
    # 查
    @property
    def name(self):
        return self.__name
    # 删
    @name.deleter
    def name(self):
        print('没有删除')
        del self.__name
    @name.setter
    def name(self,newname):
        self.__name = newname

jianghu = Person('jianghu')

# 查
print(jianghu.name)

# 删除
del jianghu.name    # 通过del去执行name函数，然后再根据函数里面的代码执行的是啥 （删除）
print(jianghu.__dict__)
print(jianghu.name)

#没有删除
# del self.__name

# 修改
jianghu.name = 'jiangxi'

print(jianghu.name)
'''
