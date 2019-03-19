#-*- coding:utf-8 -*-
# 所谓的接口类，抽象类都是基于java中来的，python本身是不存在的
# 导入抽象基类
from abc import ABCMeta,abstractmethod
# 定义一个payment父类
class Payment(metaclass=ABCMeta):   # 定义元类，默认元类为type
    @abstractmethod                 # 添加装饰器
    def pay(self,money):
        raise NotImplemented            # 没有实现pay方法时主动抛出异常


class Wechat(Payment):
    def pay(self,money):
        print('已经用微信支付%s元'%(money))


class Alipay(Payment):
    def pay(self,money):
        print('已经用支付宝支付%s元'%(money))

# 内部的函数名不是使用pay，而是其他名字
class Applepay(Payment):
    def fuqian(self,money):
        print('已经用Applepay支付%s元'%(money))

# 在外面定义一个pay函数，去使用类中的pay，只需要传递一个支付的方式对象和money,最终调用的还是类里面的pay函数
def pay(pay_kind,money):
    pay_kind.pay(money)

w1 = Wechat()
a1 = Alipay()
app = Applepay()

# w1.pay(100)
# a1.pay(200)
pay(w1,100)
pay(a1,100)
pay(app,200)
# AttributeError: 'Applepay' object has no attribute 'pay',
# 抛出异常时 报错为：TypeError: exceptions must derive from BaseException,所以新写的Applepay也需要实现pay方法

# 定义了抽象基类后报错很明显，TypeError: Can't instantiate abstract class Applepay with abstract methods pay

# 结论：
# 1、我们写的Payment其实就是一个规范，我们称为接口类，接口类，一般不实现方法
# 2、接口类一般支持多继承
# 3、抽象类不支持多继承，一般是单继承，可以实现一些方法
# 4、接口类和抽象类都是为了规范继承该类的子类