# -*- coding:utf-8 -*-
# 1、类的命名空间
#     类有自己的命名空间
#     类调用静态属性：类名.静态属性
#     类调用动态属性：类名.方法名()
#     类不能调用类的属性，报错 AttributeError: type object 'Course' has no attribute 'name'
#     对象调用属性时，如果自己的命名空间有该属性则使用自己的，如果自己的命名空间里面没有，则找类的，如果类中也没有，则报错。


# 2、对象命名空间
#     对象也有自己的独立命名空间
#     因为在对象中存在类对象指针，所以对象可以单方向去找类属性，但是类不能找对象命名空间的属性


# 3、组合，至少是有两个类
# 一个类的对象是另一个类的属性