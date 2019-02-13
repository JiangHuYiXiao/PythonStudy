# -*- coding:utf-8 -*-
# 1、程序中难免会出现错误，程序一但发生错误就会立刻停下来，不再执行后面的内容，而错误又分为两种：
    # 1、语法错误 :
    #   （这种错误，根本过不了python解释器的语法检测，必须在程序执行前就改正）
    # 2、逻辑错误（这种需要进行异常处理）
    #     res1=1/0

# 2、异常就是程序发生错误时的信号

# 3、python中的异常种类：在python中不同的异常可以用不同的类型（python中统一了类与类型，类型即类）去标识
# ，不同的类对象标识不同的异常，一个异常标识一种错误

# IndexError
list = [1,2,3]
print(list[3])          # IndexError: list index out of range

#KeyError
dic = {'name':'jianghu'}
print(dic['age'])           # KeyError: 'age'

# ValueError
str = 'hello'
int(str)        # ValueError: invalid literal for int() with base 10: 'hello'

'''
AttributeError 试图访问一个对象没有的属性，比如foo.x，但是foo没有属性x
IOError 输入/输出异常；基本上是无法打开文件
ImportError 无法引入模块或包；基本上是路径问题或名称错误
IndentationError 语法错误（的子类） ；代码没有正确对齐
IndexError 下标索引超出序列边界，比如当x只有三个元素，却试图访问x[5]
KeyError 试图访问字典里不存在的键
KeyboardInterrupt Ctrl+C被按下
NameError 使用一个还未被赋予对象的变量
SyntaxError Python代码非法，代码不能编译(个人认为这是语法错误，写错了）
TypeError 传入对象类型与要求的不符合
UnboundLocalError 试图访问一个还未被设置的局部变量，基本上是由于另有一个同名的全局变量，导致你以为正在访问它
ValueError 传入一个调用者不期望的值，即使值的类型是正确的
'''
# 4、异常处理：python解释器执行代码遇到错误后，会有相应的报错信号，程序员编写特定的代码来捕捉这个异常，
# 如果捕捉成功则进入另一个分支，这个分支就是你为其设置的逻辑，这样程序遇到错误就不会崩溃或者终止。
# 异常处理的目的：为了增强程序的健壮性和容错性。
# ret = int(input('number>>>'))           # 如果输入的是非数字，则报错ValueError: invalid literal for int() with base 10: 'ew'，这样的错误是需要进行异常处理的
# print(ret*'*')

# 4.1使用try和except就能处理异常，
    # try后面是我们需要处理的错误
    # except后面跟一个错误类型，当代码发生错误且错误类型符合的时候，就会执行except中的代码
try:            # 一定会执行该段代码
    2+'3'
    [][3]
    ret = int(input('number>>>'))
    print(ret*'*')
    list = [1,2]
    list[2]
except ValueError:          # 当出现ValueError时执行该代码
    print('你输入的内容有误，请输入数字')

# 多分支，处理多种报错，可以有多个分支，无限制
except IndexError:
    print('索引越界，超出列表最大长度')

except Exception:       # 万能异常处理
    print('你错了，老铁')
# 万能异常应该写在最下面，且可以和分支异常一起，如果存在分支异常应该先执行分支异常如果没匹配到分支异常再去执行万能异常
else:           # try中的代码没有异常中断就会执行else中的代码，一般放代码执行后的结论
    print('__________________')
finally:                # 一般放在函数里面做异常处理，做一些收尾工作
    print('程序不管怎么样都会执行的代码')         # 一般填写关闭文件，数据库等统一操作

# finally使用例子：
def func():
    try:
        f = open('file','w')
        return True         # 有return还会继续执行finally
    except:
        return False
    finally:
        print('你执行了finally')
        f.close()


# 5、什么时候用异常处理
# 有的同学会这么想，学完了异常处理后，好强大，我要为我的每一段程序都加上try...except，干毛线去思考它会不会有逻辑错误啊，这样就很好啊，多省脑细胞===》2B青年欢乐多
# try...except应该尽量少用，因为它本身就是你附加给你的程序的一种异常处理的逻辑，与你的主要的工作是没有关系的
# 这种东西加的多了，会导致你的代码可读性变差，只有在有些异常无法预知的情况下，才应该加上try...except，其他的逻辑错误应该尽量修正

# 6、万能异常正确使用方法
try:            # 一定会执行该段代码
    2+'3'
    [][3]
except Exception as error:
    print('你错了',error)          # 你错了 unsupported operand type(s) for +: 'int' and 'str'
