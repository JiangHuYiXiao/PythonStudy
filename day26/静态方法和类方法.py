# -*- coding:utf-8 -*-
# 静态方法：staticmathod
# 当这个函数与这个类，这个对象都没有关系，那就把这个方法定义成一个静态方法，用staticmathod装饰
class Login:
    @staticmethod
    def get_user_password():
        user = input('请输入用户名：')
        pwd = input('请输入密码：')
        Login(user,pwd)
    def __init__(self,name,password):
        self.name = name
        self.password = password
    def login(self):
        if user == self.name and pwd == self.password:
            print('登录成功')

Login.get_user_password()
jianghu = Login('jianghu',123)
jianghu.login()










# 类方法：classmathod
# 当这个方法的操作只涉及静态属性时，就应该用classmathod来装饰这个方法
# class Goods:
#     __discount = 0.5
#     def __init__(self,name,weight,price):
#         self.name = name
#         self.weight = weight
#         self.__price = price
#     @classmethod            # 一般类方法用于那些静态属性的修改，
#     def change_discount(cls,new_discount):          # 不用传self，但是要cls，指代的是这个类
#         cls.__discount = new_discount
#     @property
#     def price(self):
#         return self.__price*Goods.__discount*self.weight
#
# apple = Goods('apple',3,6)
# print(apple.price)
#
# Goods.change_discount(0.6)  # 把一个类中的方法改为类方法后，可以直接使用类调用，不需要依托任何对象
# print(apple.price)

# 结论：
#     1、静态方法和类方法都是用类调用。
#     2、对象也可以调用静态方法和类方法。
#     3、类方法有个默认参数cls，代表这个类。
#     4、静态方法没有默认参数，就是一个普通的函数，只是他在类里面
