# -*- coding:utf-8 -*-
# 1、查看数据类型中的内置方法
print(dir([]))

# 2、可迭代的：
'''
可以被for循环的都是可迭代的，可迭代的里面必须含有双下方法__iter__
含有__iter__方法的一定可以被for循环
可迭代不一定是迭代器，但是迭代器一定可迭代
目前可迭代的数据类型有：
list
dict
set
tuple
str
file
range
enumerate:枚举
'''

# 3、迭代器
# 定义：一个可迭代对象执行了__iter__方法就是一个迭代器 iterator
print([].__iter__())       # <list_iterator object at 0x0000000001EF33C8>
print('__next__'in dir([].__iter__()))          # True
print('__iter__'in dir([].__iter__()))          # True

# 迭代器中一定包含了__iter__和__next__方法


# 4、判断一个变量是否为迭代器
from collections import Iterable
from collections import Iterator
print(isinstance([],Iterable))      # True
print(isinstance([],Iterator))      # False 列表是可迭代，但是不是迭代器


# 5、迭代器的取值
    # next方式取值
# list = [1,2,4,5,6]
# Iterator = list.__iter__()
# print(Iterator.__next__())
# print(Iterator.__next__())

    # for方式取值

# for i in Iterator:
#     print(i)

# 6、生成器:本质就是迭代器
# 生成方式1：生成器函数，返回一个生成器，我们需要对生成器执行__iter__方法生成迭代器后进行取值

# def generator():
#     print(1)
#     yield 'a'
#
# g = generator()
# for i in g:
#     print(i)

# 7、生成器可以连续取值，如果是同一个生成器的话，不同的生成器需要重新取值
def generator():
    for i in range(500000):
        yield 'wahaha%s'%i

g = generator()
g1 = generator()
count = 0
for i in g:
    if count > 50:
        break
    count = count + 1
    print(i)
print('***',g.__next__())           # *** wahaha52
print('***',g1.__next__())          # *** wahaha0

# 8、可迭代的取值，都需要重新取值
list1 = [12,13,14,15]
for i in list1:
    if i == 13:
        break
    print(i)  # 12


for i in list1:
    print(i)  # 12,13,14,15

# 9、监听文件输出的例子
def listener(filename):
    with open(filename,mode='r',encoding='utf-8') as file:
        while True:
            line = file.readline()
            if line.strip():
                yield(line.strip())

g = listener('filename')
for i in g:
    if 'python' in i:
        print(i)

# 10、生成器的取值方式和迭代器的取值方式一样，可以通过__next__,for循环，
# 还需要特意指出一个是通过数据类型的强制转换
# list(g)  占用内存