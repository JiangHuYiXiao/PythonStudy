# -*- coding:utf-8 -*-
# 和数据结构相关的内置函数：

# python中数据类型：int,str,bool,...
# python中数据结构：就是指容器类型的数据，list，dict，tuple，set，str
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
# bytes() bytes数据类型，二进制的，
# bytearray() bytes数据类型的一个数组
# memoryview()字节类型的切片
# ord()查找字符串对应的ascii码表对应的值，按照unicode编码
# chr()查找数字对应的ascii码表对应的值，按照unicode编码
# ascii()查找对应的ascii码表对应的值，按照unicode编码
# repr()返回变量的真实数据类型，可以用于%r格式化输出
# dict()
# set()
# frozenset()不可变集合，可以作为字典的key



# format()
print(format('test','>20'))          # 右边对齐，长度为20                 test
print(format('test','<20'))          # 左边对齐，长度为20test
print(format('test','^20'))          # 居中对齐，长度为20        test

# bytes()
# bytes()的应用
#     bytes在内存中的编码方式为gbk，utf-8，
#     1、想转换编码，拿到是gbk，想转成utf-8
#     实际转换过程是经过这样一个过程：gbk---decode解码--->读到内存里unicode---encode编码--->utf-8
#     2、网络传输只能是bytes类型的二进制
#     3、内存中存储是bytes类型的二进制
#     4、照片和视频是bytes类型的二进制存储
#     5、html网页爬取得也是bytes类型的二进制

print(bytes('你好',encoding='gbk'),type(bytes('你好',encoding='gbk')))  # 表示在内存中的数据类型为bytes，编码方式为unicode转换成gbk   b'\xc4\xe3\xba\xc3'
print(bytes('你好',encoding='utf-8'),type(bytes('你好',encoding='utf-8'))) #   # 表示在内存中的数据类型为bytes，编码方式为unicode转换成utf-8   b'\xe4\xbd\xa0\xe5\xa5\xbd'
# 可以再把他解码回来
# bytes('你好',encoding='gbk') # 表示在内存中的数据类型为bytes，编码方式为gbk
print(bytes('你好',encoding='gbk').decode('gbk'),type(bytes('你好',encoding='gbk').decode('gbk')))# 表示在内存中的数据类型为str，编码方式为gbk转换成unicode

# bytearray()
b = bytearray(bytes('你好',encoding='utf-8'))
print(b)   #bytearray(b'\xe4\xbd\xa0\xe5\xa5\xbd')
print(b[0])   #196

# ord()
print(ord('1'))
print(ord('a'))

# chr()
print(chr(98))
print(chr(97))

# ascii()
print(ascii('21'))
print(ascii('号'))

# %s格式化输出
name ='jianghuyixiao'
print(('我是%s') %name)   # 我是jianghuyixiao

# %r格式化输出
name ='jianghuyixiao'
print(repr(('我是%r') %name))  # "我是'jianghuyixiao'"
age = 12
print(repr(('我%r岁') %age))  # '我12岁'





