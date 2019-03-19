# -*- coding:utf-8 -*-

# 老虎，tiger，走，游泳
# 天鹅，swan，飞，游泳,走
# 老鹰，eagle 飞，走
from abc import abstractmethod,ABCMeta          # 导入抽象基类，和元类ABCMeta

class Walk_Animal(metaclass=ABCMeta):           # 接口类
    # 加上装饰器 加上规范，必须实现方法
    @abstractmethod
    def walk(self):
        pass
class Swim_Animal(metaclass=ABCMeta):           # 接口类
    @abstractmethod
    def swim(self):
        pass

class Fly_Animal(metaclass=ABCMeta):           # 接口类
    @abstractmethod
    def fly(self):
        pass

class Tiger(Walk_Animal,Swim_Animal):    #  多继承，因为Tiger继承了Walk_Animal,Swim_Animal所以这个类必须实现walk方法和swim方法，这就是上面使用@abstractmethod的作用,也就是规范
    def walk(self):
        pass
    def swim(self):
        pass

class Swan(Walk_Animal,Swim_Animal,Fly_Animal):         # 多继承
    def walk(self):
        pass
    def swim(self):
        pass
    def fly(self):
        pass

class Eagle(Fly_Animal,Walk_Animal):         # 多继承
    def fly(self):
        pass
    def walk(self):
        pass

# 接口隔离原则：使用专门的接口，而不是使用单一的总的接口，而不该依赖那些不需要的接口
# 接口和接口类，是不同的概念，不一样
# 接口类是规范，是一个面向对象的思想，规范、
# 接口类由于是多继承，所以功能比较复杂，不容易再从类中抽取相同的内容