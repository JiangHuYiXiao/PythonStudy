#-*- coding:utf-8 -*-
# 广义上的封装是：保护代码，在python中利用对象去调用类中的属性和方法，这种面向对象的思想就是封装。
# 狭义上的封装：把类中的属性、方法隐藏起来。
class Person:
    __key = 123                         # 私有静态属性
    def __init__(self,name,passwd):
        self.name = name
        self.__passwd = passwd          # 私有属性,存储格式为_Person__passwd

    def __get_passwd(self):             # 私有方法
        print(self.__dict__)            # {'name': 'alex', '_Person__passwd': 1234}
        return self.__passwd   # 只要在内的内部使用私有属性，自动的会把：_类名带上，这样可以直接调用__passwd，外部不会自动带上

    def login(self):
        self.__get_passwd()


p1 = Person('alex',1234)
print(p1.name)
# print(p1.passwd)      # AttributeError: 'Person' object has no attribute 'passwd'不能直接通过对象调用
print(p1.__dict__)      # {'name': 'alex', '_Person__passwd': 1234}
# 私有属性调用方法：
    # 通过：对象._类名__私有变量名
print(p1._Person__passwd)           # 1234

# 外部定义私有属性
p1.__high = 1           # {'name': 'alex', '_Person__passwd': 1234, '__high': 1},外部定义私有属性不会加上_类名

    # 通过：类部方法进行调用
print(p1.get_passwd())              # 1234


# 总结：
    # 所有的私有都是在左边加上双下划线
    # 都是在类的类部使用，一般不建议在外部使用
    # 私有属性
    # 私有方法
    # 私有静态属性

