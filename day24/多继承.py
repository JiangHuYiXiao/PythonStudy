# -*- coding:utf-8 -*-
# 1、钻石继承案例

class A:
    def func(self):
        print('A')

class B(A):
    pass
    # def func(self):
    #     print('B')

class C(A):
    pass
    # def func(self):
    #     print('C')

class D(B,C):
    pass
    # def func(self):
    #     print('D')

d = D()
d.func()
# 继承顺序为：D,B,C,A


# 2、小乌龟继承案例
class A:
    def func(self):
        print('A')

class B(A):
    pass
    # def func(self):
    #     print('B')

class C(A):
    pass
    # def func(self):
    #     print('C')

class E(B):
    pass
    # def func(self):
    #     print('E')
        
class F(C):
    pass
    # def func(self):
    #     print('F')

class D(E,F):
    pass
    # def func(self):
    #     print('D')

d = D()
d.func()
# 可以通过mro查询继承顺序只在新式类中存在
print(D.mro())          # [<class '__main__.D'>, <class '__main__.E'>, <class '__main__.B'>, <class '__main__.F'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]

# 继承顺序为：D,E,B,F,C,A
# 总结：
#   python3的新式类中多继承的顺序结论：
# 1、先找自己，自己没有找父类。
# 2、再看父类上面是否还有父类，以及是否父类的父类只能通过这个这个路径找到，如果只能通过这个路径找到，则先找这个父类的父类。
# 3、如果另一个父类，也可以找到这个父类的父类，则先找另一个父类。
# 4、最后找的是最上面的那个父类。
# 5、广度优先，其次再是深度，
# 6、新式类都要继承object类，
# 7、就近原则

#    python2.7中的经典类是深度优先，新式类是广度优先，新式类都要继承object类

# super的本质：
# 1、super只在python3中存在
# 2、super调用的不是父类，而是根据广度优先的调用者的位置来的
class A:
    def func(self):

        print('A')

class B(A):
    def func(self):
        super().func()
        print('B')

class C(A):
    def func(self):
        super().func()
        print('C')

class D(B,C):
    def func(self):
        super().func()
        print('D')

d = D()
d.func()

# 因为继承顺序为：D,B,C,A，所以D的super是B,B的super是C,C的super是A,所以结果为：A,C,B,D