# -*- coding:utf-8 -*-

# python天生支持多态
# 1、多态指的是一类事物有多种表现形态，比如动物有人、猪、狗
import abc
class Animal(metaclass=abc.ABCMeta): #同一类事物:动物
    @abc.abstractmethod
    def talk(self):
        pass

class People(Animal): #动物的形态之一:人
    def talk(self):
        print('say hello')

class Dog(Animal): #动物的形态之二:狗
    def talk(self):
        print('say wangwang')

class Pig(Animal): #动物的形态之三:猪
    def talk(self):
        print('say aoao')


# 文件有多种形态：文本文件，可执行文件
import abc
class File(metaclass=abc.ABCMeta): #同一类事物:文件
    @abc.abstractmethod
    def click(self):
        pass

class Text(File): #文件的形态之一:文本文件
    def click(self):
        print('open file')

class ExeFile(File): #文件的形态之二:可执行文件
    def click(self):
        print('execute file')


# 2、多态性：不同的形态实现相同的方法，然后根据分支不同，实现不一样
class Payment:
    pass

class Wechat(Payment):
    def pay(self,money):
        print('已经用微信支付%s元'%(money))


class Alipay(Payment):
    def pay(self,money):
        print('已经用支付宝支付%s元'%(money))

def pay(pay_kind,money):    # 统一支付入口
    pay_kind.pay(money)

w1 = Wechat()
a1 = Alipay()
pay(w1,11)
pay(a1,12)

# 鸭子类型：python就是鸭子类型，默认支持多态，因为python数据传递时不需要指定数据类型
# 不崇尚继承父类的相似
# 我只是自己实现我自己的代码
# 如果两个类刚好显示，并不产生父类的子类的兄弟关系，而是鸭子类型。
# 比如说list，tuple的index，slic方法

# 优点：松耦合，每个相似的类之间都没有影响
# 缺点：太随意了
class List:
    def __len__(self):
        pass
class Tuple:
    def __len__(self):
        pass
def len(l_t):
    return l_t.__len__()

l = List()
len(l)      # 这两个类List，Tuple就是鸭子类型
t = List()
len(t)

# 其他语言，如java需要定义父类，python不需要定义一个父类
class Foo:
    pass

class List(Foo):
    def __len__(self):
        pass
class Tuple(Foo):
    def __len__(self):
        pass
# def len(Foo l_t):   # 指定是哪个父类
#     return l_t.__len__()

l = List()
len(l)

# 接口类和抽象类，在python中的应用并不是非常必要
#