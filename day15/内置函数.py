# -*- coding:utf-8 -*-
# 内置函数分类：
# 一、作用域相关
# 1、globals() 一定返回全局作用域的所有变量
# 2、locals() 如果在全局则返回全局作用域的所有变量，如果在局部则返回局部作用域的所有变量
a = 10
def func(*args,**kwargs):
    b = 20
    print('***',b)
    print(locals())         # 返回局部作用域的的所有变量

print(globals())            # 返回全局作用域的所有变量
func()


# 二、其他
# 1、输入输出
# 输入input()

res = input('请输入：')
print(res)

# 输出print()   def print(self, *args, sep=' ', end='\n', file=None):
# end 指定输出的结束符
print('江湖一笑\n') # 默认会换行end='\n',可以自己定义end值
print('江湖一笑',end='')
print('江湖一笑',end='888888')   # 江湖一笑江湖一笑
print('江湖一笑')   # 江湖一笑江湖一笑888888江湖一笑

# sep指定多个不同元素的连接符
# print('江湖一笑','jianghuyixiao',sep='==')   #江湖一笑==jianghuyixiao

# file,默认输出到屏幕，但是可以自己修改到指定文件
f = open('file',mode='w+',encoding='utf-8')
print('woqu',file=f)            # 输出到指定文件file里面去了
f.close()

# 2、查看（变量、函数）对象的内置属性名
# dir()
print(dir([]))
print(dir(2))

# 3、帮助
# help()  比dir（）更详细，dir（）给出的是方法名
help(list)

# 4、调用相关
# callable() 判断这个变量是否可以调用，如果变量名是函数则可以调用，其他不可调用
print(callable(print))  # True
print(callable(12)) # False

# 5、模块相关
# import,导入模块，其实内部使用的就是双方法__import__()
import time

# 内部
t = __import__('time')
print(t.time())

# 如果某个方法属于某个数据类型内部的方法，则使用.调用
# 如果某个方法不依赖于任何数据类型则直接调用，---只有内置函数、自定义函数支持。

# 6、文件操作相关
# open() 操作文件

# 7、内存相关
# id() 查看变量的内存地址，
# hash() 查看不可变数据类型的哈希值,对于相同的可哈希的数据，在一次执行中的hash值时不可变的
# 我們字典的查找就是通過查找鍵的hash值，去查找值。所以查詢速度很快
list =[1,2,3]
print(id(list))

print(hash(1212312231231))
print(hash('isjofijwoeiroweiruweori'))
print(hash([1,3,4]))     # TypeError: unhashable type: 'list'

# 8、字符串类型代码的执行:执行字符串类型代码
# exec()        # 执行字符串类型代码，没有返回值，一般用在处理简单的流程
# eval()        # 执行字符串类型代码，有返回值,只能用在你明确知道你要执行的代码是什么,就是写死的
# compile       # 把字符串代码进行编译，实际执行的还是要exec，或者eval
exec('print(123)')
eval('print(123)')
print(exec('1+2+3'))  # None
print(eval('1+2+3'))

code = '''for i in range(10):
    print(i*'*')
'''
exec(code)


code1 = '''for i in range(10):
    print(i)
'''
compile1 = compile(code1,'','exec')
exec(compile1)


# 三、迭代器/生成器相关
# __next__()查看迭代器、生成器的下一个值,一般都是用next()
# __iter__() 可迭代的调用iter方法生成一个迭代器
# range() 可迭代的，循环取值
class A:
    def __iter__(self):
        pass
    def __next__(self):
        pass
a = A()
a.__next__()
a.__iter__()
next(a)
iter(list)
# 迭代器 = 可迭代的.__iter__()
# 迭代器 = iter(可迭代的)

# 迭代器.__next__()
# next(迭代器)

range(10)
range(1,11,2)
print('__iter__' in dir(range(10))) # True 可迭代的
print('__next__' in dir(range(10))) # False 不是一个迭代器
print('__next__'in dir (iter(range(2)))) # True 被iter调用后就是一个迭代器

# 四 、基础数据类型相关
# 1、和数字相关
# 1.1 数据类型
# bool()
# int()
# float() 有限循环小数，无限循环小数
# complex(()  复数，也就是实数+虚数，3+2j
print(bool(0))          # False
print(bool(2))          # True
print(bool('ewr'))          # True

print(int(True))         # 1
print(int(False))         # 0
print(int('21312'))         # 21312


# 1.2 进制转换
# bin()二进制
# oct()八进制
# hex()十六进制
print(bin(12))          # 0b1100
print(oct(12))          # 0o14
print(hex(12))          # 0xc

# 1.3 数学运算
# abs()#绝对值
# divmod()#除余
# round()#取精确值
# pow()#幂运算
# sum()#求和,需要给可迭代的 sum(iterable,start)
# min()#最小值
# max()#最大值
print(abs(-1))
print(divmod(11,3))   #(3, 2)3,是商，余2，div是除数，mod是取余数
print(round(12.3587,1)) # 12.4 取小数点后一位，四舍五入
print(pow(2,5))  # 2的5次方
print(sum([1,324],1))  # 1+324+1
print(sum((1,324),1))  # 1+324+1
# min(iterable,key,defult)
# min(*args,key,defult)
print(min([1,23,32]))
print(min(1,23,32))
print(min(1,23,32,-3))
print(min([1,-23,32],key=abs))  # 1 先取绝对值再去取最小值

print(max([1,23,32]))
print(max(1,23,32))
print(max(1,23,32,-3))
print(max([1,-23,32,-65],key=abs))  # 32 先取绝对值再去取最大值

