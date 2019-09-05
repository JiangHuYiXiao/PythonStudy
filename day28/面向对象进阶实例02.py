# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/9/3 16:15
# @Software       : PythonStudy
# @Python_verison : 3.7
'''
# 1、namedtuple
# nametuple是tuple的一个子类
# namedtuple能够用来创建类似于元祖的数据类型，除了能够用索引来访问数据，能够迭代，还能够方便的通过属性名来访问数据。
# 来解释一下nametuple的几个参数，Friend=namedtuple(‘Friend’,['name', 'age', 'email'])为例，其中’Friend’是这个namedtuple的名称，
# 后面的'name', 'age', 'email’这个字符串中三个用逗号隔开的字符告诉我们，我们的这个namedtuple有三个元素，分别名为name,age和email。
# 我们在 创建它的时候可以通过f1 = Friend('xiaowang', 33, 'xiaowang@163.com')这种方式，这类似于Python中类对象的使用。
# 而且，我们也可以像访问类对象的属性那样使用f1.name这种方式访问namedtuple的元素。
from collections import namedtuple

Friend = namedtuple("Friend", ['name', 'age', 'email'])   # 相当于面向对象的创建类

f1 = Friend('xiaowang', 33, 'xiaowang@163.com')         # 相当于面向对象的创建对象，实例化
print(f1)
print(f1.age)
print(f1.email)
f2 = Friend(name='xiaozhang', email='xiaozhang@sina.com', age=30)
print(f2)

name, age, email = f2
print(name, age, email)
'''
# 2、进阶实例   纸牌
import json
from collections import namedtuple
from random import choice
from random import shuffle
Card = namedtuple('Card',['rank','suit'])           # rank 大小，suit 花色
# c1 = Card(2,'红心')
# print(c1)
# print(c1.suit)
# print(c1.rank)
class FranchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = ['红心','方板','梅花','黑桃']

    def __init__(self):
        self._cards = [Card(rank,suit) for rank in FranchDeck.ranks
                                        for suit in FranchDeck.suits]

    def __len__(self):
        return len(self._cards)           # 不实现__len__方法时，报错：TypeError: object of type 'FranchDeck' has no len()

    def __getitem__(self, item):
        return self._cards[item]

    def __setitem__(self, key, value):          # 不实现setitem方法会报错，TypeError: 'FranchDeck' object does not support item assignment
        self._cards[key] = value

    def __str__(self):      # 不实现__str__方法返回的是一个对象的内存地址
        return json.dumps(self._cards,ensure_ascii=False)
deck = FranchDeck()
print(deck)
print(deck[0])      # 要通过这种方式查询，所以必须实现setitem方法
print(choice(deck))          # 随机抽一张牌
print(deck)

shuffle(deck)   # 打乱牌
print(deck[1])
print(deck[:4])


