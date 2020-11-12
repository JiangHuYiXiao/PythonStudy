# -*- coding:utf-8 -*-
# 1、int 实数（数字、小数、负数）
#
# 2、bool 布尔，（只有True或者False）用于判断
#
# 3、str 字符串（在python中用引号括起来的都是都是字符串），字符串用于存储少量数据

# 4、list 列表（用中括号表示用于存储大量数据）list[],百万级至千万级
# 列表有序且可变
list1 = [1,2,3,[12,13]]
print(list1)
print(type(list1))
# 5、tuple元组（） 有序不可变
# 元组：也是一个数据的集合，也是有序的，但是它不可变，也称作为只读列表，用小括号()
# 特性：元组本身不可变，但是里面可以包含列表，所以元组间接也是可变的。
tuple1 = (1,2,334,'jianghu')
print(tuple1)
print(type(tuple1))
# 6、dict 字典，用大括号表示，里面是包含键值对的，一个键对应一个值，用于存储大量数据，但是一般用于存储关系型数据
# 1、字典是可变，无序的数据集合(没有索引，因为可以通过key查询)
# 2、字典格式是key-value的数据类型,key是不可变的，key必须可以hash，value可变
# 3、查找速度快（是通过比二分法更快的方式进行查找的，通过hash函数将key转为数字，然后比较大小，进行查找）所以key必须可以hash
# 4、可存放任意多个值不唯一，
# 定义一个空字典：
dict2 = {}
dict = {'name':'jianghu','age':'17'}
print(dict)
print(type(dict))

# 7、集合是一个无序的，不重复的数据集合，用{}表示
# 定义一个空集合使用：
a = set()
print(type(a))
set = {11,12,'12231'}
print(set)
print(type(set))
