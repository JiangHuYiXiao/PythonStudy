#-*- coding:utf-8 -*-
# 在内置的数据类型（list，dict，tuple，set）上面，collcetion又增加了一些额外的数据类型counter,deque,defaultdict,orderedict
# 在内置数据类型（dict、list、set、tuple）的基础上，collections模块还提供了几个额外的数据类型：Counter、deque、defaultdict、namedtuple和OrderedDict等。
#
# 1.
# namedtuple: 生成可以使用名字来访问元素内容的tuple
#
# 2.
# deque: 双端队列，可以快速的从另外一侧追加和推出对象
#
# 3.
# Counter: 计数器，主要用来计数
#
# 4.
# OrderedDict: 有序字典
#
# 5.
# defaultdict: 带有默认值的字典
#
# namedtuple
# 我们知道tuple可以表示不变集合，例如，一个点的二维坐标就可以表示成：
#
# >> > p = (1, 2)
# 但是，看到(1, 2)，很难看出这个tuple是用来表示一个坐标的。
#
# 这时，namedtuple就派上了用场：
#
# 复制代码
# >> > from collections import namedtuple
# >> > Point = namedtuple('Point', ['x', 'y'])
# >> > p = Point(1, 2)
# >> > p.x
# 1
# >> > p.y
# 2
# 复制代码
# 类似的，如果要用坐标和半径表示一个圆，也可以用namedtuple定义：
#
# # namedtuple('名称', [属性list]):
# Circle = namedtuple('Circle', ['x', 'y', 'r'])
# deque
# 使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低。
#
# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：
#
# >> > from collections import deque
# >> > q = deque(['a', 'b', 'c'])
# >> > q.append('x')
# >> > q.appendleft('y')
# >> > q
# deque(['y', 'a', 'b', 'c', 'x'])
# deque除了实现list的append()
# 和pop()
# 外，还支持appendleft()
# 和popleft()，这样就可以非常高效地往头部添加或删除元素。
#
# OrderedDict
# 使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。
#
# 如果要保持Key的顺序，可以用OrderedDict：
#
# 复制代码
# >> > from collections import OrderedDict
# >> > d = dict([('a', 1), ('b', 2), ('c', 3)])
# >> > d  # dict的Key是无序的
# {'a': 1, 'c': 3, 'b': 2}
# >> > od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
# >> > od  # OrderedDict的Key是有序的
# OrderedDict([('a', 1), ('b', 2), ('c', 3)])
# 复制代码
# 注意，OrderedDict的Key会按照插入的顺序排列，不是Key本身排序：
#
# >> > od = OrderedDict()
# >> > od['z'] = 1
# >> > od['y'] = 2
# >> > od['x'] = 3
# >> > od.keys()  # 按照插入的Key的顺序返回
# ['z', 'y', 'x']
# defaultdict
# 有如下值集合[11, 22, 33, 44, 55, 66, 77, 88, 99, 90...]，将所有大于
# 66
# 的值保存至字典的第一个key中，将小于
# 66
# 的值保存至第二个key的值中。
#
# 即： {'k1': 大于66, 'k2': 小于66}
# 原生字典解决方法
# defaultdict字典解决方法
# 使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict：
#
# 例2
#
# Counter
# Counter类的目的是用来跟踪值出现的次数。它是一个无序的容器类型，以字典的键值对形式存储，其中元素作为key，其计数作为value。计数值可以是任意的Interger（包括0和负数）。Counter类和其他语言的bags或multisets很相似。
#
# c = Counter('abcdeabcdabcaba')
# print
# c
# 输出：Counter({'a': 5, 'b': 4, 'c': 3, 'd': 2, 'e': 1})