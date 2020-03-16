# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/3/16 16:46
# @Software       : Python_study
# @Python_verison : 3.7
class Person:
    def __init__(self,*args):
        self.name=args[0]
        self.age=args[1]
    def talk(self):
        print("多交流多沟通")
        return self         # 返回对象后就可以进行链式操作
    def run(self):
        print("gogo")
        return self         # 返回对象后就可以进行链式操作

jianghu = Person('jianghu',19)
jianghu.run().talk()
jianghu.talk().run()