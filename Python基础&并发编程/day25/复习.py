# -*- coding:utf-8 -*-
# python对象的三大特性：（继承、多态、封装）
# 1、继承
    # 一个子类继承一个父类
    # 一个父类可以被多个子类继承
    # 一个子类可以继承多个父类
    # 子类对象调用，子类中有则先使用子类的，找不到则使用父类的
    # 子类可以使用父类的属性，但是父类不能使用子类的属性，各个继承同一个子类是没有关系的
    # 查看子类继承的是哪个父类：（字类名.__base__）
    # python中的新式类都有父类，因为他们都继承与object类
    # 继承表示的是一个什么是什么的关系，我是人
    # 组合表示的是一个，什么有什么的关系，我有生日

# 2、派生
    # 派生是子类所拥有的属性或者方法，父类不具有，
    # 有派生属性和派生方法


# 3、子类使用父类的功能：
    # 方法1：
        # 子类使用父类属性的方式为：（父类名.__init__(self,属性1,属性2)）
        # 子类使用父类方法的方式为：（父类名.方法名(self)）

    # 方法2：
        # 子类使用父类属性的方式为：（super().__init__(属性1,属性2)）
#       # 子类使用父类方法的方式为：（super().方法名()）


# 4、super本质
    # super只在python3中存在的
    # super的本质不是调用父类，而是根据广度优先的继承顺序的位置来的

# 5、多继承

# 继承顺序首先是就近原则
# 继承顺序然后是广度优先，最后是深度
# 如果只能根据唯一路径找到父类，则先深度，后广度
# 钻石继承，小乌龟继承
# 可以通过（类名.mro()）查询类的集成顺序