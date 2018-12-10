# -*- coding:utf-8 -*-
# 一、内置函数
'''
# 1、作用域相关(2)
globals()           # 返回全局作用域的变量
locals()            # 返回局部作用域的变量

# 2、迭代器、生成器相关(3)
list = [1,2,3]
next(list)          # 内部其实是__next__()
iter(list)          # 内部其实是__iter__()
range(100)
'''
# 3、其他（12）
#     1、输入输出
#             input()
#             print()
#                 print('aaa','bbb',sep='***')            # sep,输出多个值时连接符
#                 print('aaa','bbb',sep='***',end='###')            # end,行尾输出符
#                 f = open('fuxi',mode='w',encoding='utf-8')
#                 print('aaa','bbb',sep='***',end='###',file=f)            # end,行尾输出符
#     2、内存
#             id()            # 返回变量的内存地址
#             hash()          # 返回可哈希的哈希值，只有不可变数据类型可以哈希，
#     3、帮助
#             dir()           # 查看方法名
#             help()          # 查看详细的帮助
#     4、文件操作相关
#             open()
#     5、函数调用
#             callable() 用于判断对象是否可调用
#     6、模块相关
#             __import__()
#     7、字符串类型代码的执行
#             eval()  执行字符串代码，有返回值，一般用在知道明确返回什么
code = 'print(123)'
eval(code)
#             exec()    无返回值，一般用在简单流程上
code1 = '''
for i in range(10):
    print(i)
'''
exec(code1)
#             compile  编译字符串类型的代码

res = compile(code1,'','exec')
exec(res)

# 4、基础数据类型相关
#     1、数据类型
#         int()
#         bool()
#         float() 有限循环小数、无限循环小数
#         complex复数，1+2j
#     2、进制转换
#     bin()   # 二进制
#     oct()   # 八进制
#     hex()   # 16进制
print(bin(12)) # 0b1100
print(oct(12)) # 0o14
print(hex(12)) # 0xc

    # 3、数学运算
#     sum()   # 求和,需要给可迭代的 sum(iterable,start)
#     max()
#     min()
#     abs()   # 绝对值
#     divmod()    # 除余
#     round() # 精确值
#     pow()   # 幂运算
# min(iterable,key,defult)
# min(*args,key,defult)

    # 4、数据集合
#     dict()
#     set()
#     frozenset()不可变集合，可以作为字典的key

    # 5、序列
#     list()
#     tuple()
#     reversed()返回一个新的反序的迭代器，为了节省内存空间，
#     slice() 切片
#     str()
#     format()格式化输出
print(format('test','>20'))
print(format('test','<20'))
print(format('test','^20'))

#     bytes(),bytes数据类型，二进制
#     bytearray()bytes数据类型的一个数组
#     ascii()转换出参数的ascii
#     ord()将字符串的ascii转换出来
print(ord('q'))
#     chr()将数字的ascii转换出来
print(chr(97))
#     memoryview() 字节类型的切片
#     repr() 用于%r的格式化输出，返回实际数据类型
name = 'jianghu'
age = 18
print(repr('我的名字%r'%name))
print(repr('我的年龄%r'%age))
    # 6、相关内置函数
    #     len() 返回长度
    #     map() 返回元素个数和调用前一致
    #     filter() 过滤，返回的元素少于过滤前的
    #     zip() 将两个列表组合起来，最小规则
    #     all() 是否全部为True，全是True则为True
    #     any() 是否有一个为True，有一个True则为True
    #     enumerate() 枚举值
    #     sorted() 排序，生成一个新的序列

# 5、反射相关（后面补充）

# 6、面向对象相关（后面补充）

# 二、匿名函数
# 只能写在一行
def func(x):
    return (x+1)
res = func(11)
print(res)
func1 = lambda x :x+1
res1 = func1(12)
print(res1)
# 匿名函数一般都是和这几个函数一起使用（max，min，filter，map，sorted）

# 可迭代对象的取值方式：
#     1、可以通过数据类型强制转换取值
#     2、next
#     3、for循环
#     4、send


