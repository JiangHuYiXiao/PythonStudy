# -*- coding:utf-8 -*-
# 1、静态属性为不可变数据类型
'''
class Course:
    language = 'chinese'
    def __init__(self,*args):
        self.name = args[0]
        self.teacher = args[1]
        self.period = args[2]
        self.price = args[3]
    def func(self):
        print('%s个月学结束'%(self.period))
python = Course('python','alex',6,18000)
linux = Course('Linux','oldboy',6,10000)
# 类的命名空间
    # 1、类调用静态属性
print(Course.language)
    # 2、类调用静态属性
Course.func(python)
    # 3、类调用类的属性
# print(Course.name)          # AttributeError: type object 'Course' has no attribute 'name',得出结论，类不能使用对象的属性，因为如果有两个对象，应该使用谁的呢，就会混乱
    # 4、对象调用静态属性
print(python.language)          # chinese
python.language = 'english'    # 在对象的命名空间里面给对象加上一个language属性，但是不会修改类中的静态属性的值,这样之后python.language始终用的是python自己的language属性
# del python.language只有使用把这个属性删除后，python就是会再次使用类的静态属性

print(python.language)          # english
print(Course.language)          # chinese
Course.language = 'french'
print(python.__dict__)          # {'name': 'python', 'teacher': 'alex', 'period': 6, 'price': 18000, 'language': 'english'}
print(Course.language)          # french
print(python.language)          # english   python对象的属性不会改，因为python用的是自己的language属性，
print(linux.language)           # french    linux用的是Course类的language属性

# 由上可以得出结论：
# 1：对象中的属性可以找到类中的属性，这是因为在对象的命名空间有个类对象指针，指向类，所以对象调用属性时，
# 先查看对象的命名空间下面有吗，有的话就使用自己的，没有就找类的，如果类还没没有就不会找了，报错。
# 2、类不能调用对象的属性
# 3、调用静态属性时，尽量使用类去调用，不要使用对象去调用。因为用对象去操作后可能永远就不会使用静态属性了
'''
# 2、静态属性为可变数据类型
class Course1:
    language = ['chinese']
    def __init__(self,*args):
        self.name = args[0]
        self.teacher = args[1]
        self.period = args[2]
        self.price = args[3]
    def func1(self):
        print('%s个月学结束'%(self.period))
python1 = Course1('python','alex',6,18000)
linux1 = Course1('Linux','oldboy',6,10000)
# 1、使用类修改静态属性
Course1.language[0] = 'german'
print(Course1.language)         # ['german']
print(python1.language)         # ['german']
print(linux1.language)          # ['german']
# 2、使用对象修改静态属性
# python1.language[0] = 'english'   # 这样是修改列表中第0个元素，所以对象的language都会修改
# print(Course1.language)         # ['english']
# print(python1.language)         # ['english']
# print(linux1.language)          # ['english']
# 3、为对象创建一个language属性
python1.language = ['english']   # 这样是修改列表中第0个元素，所以对象的language都会修改
print(Course1.language)         # ['german']
print(python1.language)         # ['english']
print(linux1.language)          # ['german']

# 由上得出结论，
# 1、对于不可变数据类型，类中的静态属性最好用类名去调用操作。
# 2、对于可变数据类型，修改是共享的，使用对象重新赋值是独立的。


