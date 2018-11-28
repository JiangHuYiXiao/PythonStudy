#-*- coding:utf-8 -*-
# 1、学习到目前为止，我们所学过的可以被for循环的有：这些其实都是可迭代对象
'''
1、字符串，str
2、列表，list
3、枚举，enumerate,返回索引和值，针对于所有可迭代对象
a = 'jsjdff'
for i in enumerate(a):
    print(i)

4、字典，dict
5、元组，tuple
6、集合，set
7、range()
8、file，文件句柄
'''
# 2、查看各个数据类型的内置方法可以通过dir()方法
print(dir([]))
print(dir({}))
print(dir(()))
print(dir(''))
print(dir(''))
# ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

# 3、想要查看上面第一个里面说的可迭代对象共有的方法
# 我们通过dir（）返回的数据类型为列表，想要查询共有的方法，需要通过集合
res = set(dir([]))&set(dir({}))&set(dir(()))&set(dir(range))&set(dir(''))
print(res)
# {'__iter__', '__init__', '__format__', '__ge__', '__init_subclass__', '__class__', '__getitem__', '__sizeof__', '__doc__', '__str__', '__lt__', '__new__', '__reduce_ex__', '__ne__', '__getattribute__', '__delattr__', '__contains__', '__setattr__', '__eq__', '__repr__', '__dir__', '__reduce__', '__le__', '__hash__', '__subclasshook__', '__len__', '__gt__'}

# 4、int是不可被for循环的,其实质就是不可迭代
for i in 123:
    print(i)   # TypeError: 'int' object is not iterable（不可迭代的）

# 5、说明可以被for循环的对象都是有可迭代的方法，这个方法就是__iter__
# 所以，在以后我们判断一个对象是否可以迭代就直接可以通过判断是否存在__iter__方法，存在就是可以迭代，不存在就是不可以迭代，我们自己开发对象可以给他加上__iter__方法，然后它就可以迭代了。
print(dir(int))
# 判断int数据类型是否包含__iter__方法
print('__iter__' in dir(int))    # False
print('__iter__' in dir(list))    # True
print('__iter__' in dir(dict))    # True
print('__iter__' in dir(tuple))    # True
print('__iter__' in dir(set))    # True
print('__iter__' in dir(range(10)))    # True
print('__iter__' in dir(enumerate([])))    # True
print('__iter__' in dir(bool()))    # False

# 6、这样我们就可以得出迭代器的定义了:一个可迭代对象执行了__iter__方法的返回值就是一个迭代器iterator
print([].__iter__())    # <list_iterator object at 0x0000000001F33898>

# 7、再查看下迭代器内部有哪些方法
print(dir([].__iter__()))  # ['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__length_hint__', '__lt__', '__ne__', '__new__', '__next__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__']

# 8、查询可迭代对象和迭代器内置方法差异，用迭代器里面的方法-可迭代对象里面的方法，得出来就是迭代器才有得方法
res = set(dir([].__iter__())) - set(dir([]))
print(res)    # {'__next__', '__length_hint__', '__setstate__'}
print([1,'3ew'].__iter__().__length_hint__())   # __length_hint__返回函数个数
l = [1,3,45,56]
iterator = l.__iter__()
print(iterator.__next__())      # 1
print(iterator.__next__())   # 3  取值，连续取值


# 综上所诉：
# 1、只要含有__ieter__方法的都可以被for循环，都是可迭代的iterable
# 2、[].__iter__() 就是一个迭代器，只有迭代器才含有 __next__（），__length_hint__（），__setstate__()方法，__next__是关键方法，用于连续取值，__length_hint__（）用于计算元素个数
# 只要含有__iter__方法都是可迭代的，---可迭代协议
# 内部同时含有__next__和__iter__方法的就是迭代器，必须同时含有这两个方法---迭代器协议，
print('__iter__' in dir([].__iter__()))         # True
print('__next__' in dir([].__iter__()))         # True


from collections import Iterable
from collections import Iterator
# print(isinstance([],Iterable))          # True 列表是可迭代的，但是不是迭代器
# print(isinstance([],Iterator))          # False 列表是可迭代的，但是不是迭代器
# isinstance用于判断是否是后面指定的数据类型

# 可以自己创建一个数据类型
class A:
    def __iter__(self):
        pass
    def __next__(self):
        pass
a = A()
print(isinstance(a,Iterable))  # True
print(isinstance(a,Iterator))  # True  a,是可迭代的也是迭代器

class B:
    # def __iter__(self):
    #     pass
    def __next__(self):
        pass
b = B()
print(isinstance(b,Iterable))  # False
print(isinstance(b,Iterator))  # False  a,不是可迭代的也不是迭代器

class B:
    def __iter__(self):
        pass
    # def __next__(self):
    #     pass
b = B()
print(isinstance(b,Iterable))  # True
print(isinstance(b,Iterator))  # False


# 迭代器一定可以迭代
# 但是可迭代不一定是迭代器



# 9、在以后实际工作中，有两种情况我们可以判断或者猜测给的对象是一个可迭代器
#     1、明确指出对象为Iterator
#     2、根据实际业务理解应该给我们返回很多值，实际却只给了一个值，我们就可以猜测这个是一个迭代器，我们可以对它进行循环取值，因为迭代器都是可迭代的通过for循环或者迭代器的内置方法__next__()

# 只有可迭代对象才可以for循环
# 如果我们新遇到一个变量是不是可以用for循环取值，我们可以判断改变量里面是否含有__iter__()方法,如果有则可以用for循环，如果没有则不可以用for循环

# 10、for循环的本质就是迭代器，循环到最后会抛一个异常StopIteration
list = [11,12,13]
for i in list:
    print(i)

Iterator = list.__iter__()

print(Iterator.__next__())
print(Iterator.__next__())
print(Iterator.__next__())

# 11、迭代器的好处
    # 可以从容器类型中一个一个取值，且可以全部取到
    # 节省内存空间，不会在内存中占用大块内存，而是随着循环每次生成一个，或者每次next生成一个

# 自己写个for循环
list = [12,423,4353,'dd']
Iterator = list.__iter__()
while True:
    print(Iterator.__next__())

# StopIteration异常后续可以处理


# 12、通过迭代器生成wahaha后面添加序列这样的100000


def func():
    for i in range(100001):
        print('wahaha%s'%(i))

func()

