# -*- coding:utf-8 -*-
# 静态方法：staticmathod
# 类方法：classmathod
class Goods:
    __discount = 0.5
    def __init__(self,name,weight,price):
        self.name = name
        self.weight = weight
        self.__price = price
    @classmethod            # 一般类方法用于那些静态属性的修改，
    def change_discount(cls,new_discount):
        cls.__discount = new_discount
    @property
    def price(self):
        return self.__price*Goods.__discount*self.weight

apple = Goods('apple',3,6)
print(apple.price)

Goods.change_discount(0.6)  # 把一个类中的方法改为类方法后，可以直接使用类调用，不需要依托任何对象
print(apple.price)


