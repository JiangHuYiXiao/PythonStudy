#-*- coding:utf-8 -*-

# 1、封装的基础
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


# 2、get方法获取私有属性，set方法修改私有属性
# 举例：
class House:            # 父类
    def __init__(self,name,width,height):
        self.__name = name                # 作为私有就是，为了不让在类的外面进行修改，导致错误
        self.__width = width            # 私有属性，作为为了是不让别人用，自己用来计算面积
        self.__height = height

    def area(self):
        return self.__width*self.__height

    # 获取私有属性值
    def get_name(self):
        return self.__name

    # 修改私有属性值
    def set_name(self,new_name):
        if type(new_name) is str and new_name.isdigit() == False:       # 保护私有属性不会随便修改
            self.__name = new_name
        else:
            print('不合法的姓名')

sz = House('jianghu',120,100)
print(sz.area())

# 类的外部修改属性
# sz.name = 2
# print(sz.name)          # 这样就导致name属性值，不能见名知意了，所以可以把name进行私有化

sz.set_name('22')           # 不合法的姓名
print(sz.get_name())


# 3、父类的私有属性不能被子类调用
class House:            # 父类
    def __init__(self,name):
        self.__name = name                # 作为私有就是，为了不让在类的外面进行修改，导致错误

class Son(House):
    print(House.name)           # AttributeError: type object 'House' has no attribute 'name'

# 会用到私有的概念地方有：
    # 1、隐藏这个属性不想被类的外部调用
    # 2、不想这个属性被随意改变
    # 3、不想子类继承父类的这个属性
