# -*- coding:utf-8 -*-
# 和数据结构相关的内置函数：

# python中数据类型：int,str,bool,...
# python中数据类型：就是指容器类型的数据，list，dict，tuple，set，str
# 1、列表和元组
# list()用于数据类型强制转换
# tuple()用于数据类型强制转换

# 2、序列相关的内置函数
# reversed()返回一个反序的迭代器，为了节省内存空间
# slice() 切片
list1 = [1,324,-1,234,9,23]
list2 = reversed(list1) # 返回反序的一个迭代器,之前的列表没有修改，然而reverse是在原来的列表上修改
for i in list2:
    print(i)
print(list2)            # <list_reverseiterator object at 0x0000000001EE39B0>

sli = slice(1,5,2)
print(sli)
print(list1[sli])

# 3、字符串
# str()
# format()格式化输出
# bytes()
print(format('test','>20'))          # 右边对齐，长度为20                 test
print(format('test','<20'))          # 左边对齐，长度为20test
print(format('test','^20'))          # 居中对齐，长度为20        test

