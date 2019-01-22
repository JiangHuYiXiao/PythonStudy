# -*- coding:utf-8 -*-

# 1、模块导入import
import demo         # 输出结果为 in demo.py

# import 具体做了以下事：

#     1、找到模块
#     2、创建这个模块的命名空间
#     3、把文件中的名字都放到命名空间里面

# 2、模块中方法的调用
demo.read()         # in read

# 3、模块中变量的使用
print(demo.money)

# 4、通过import方式导入的模块和在执行的文件中存在相同的方法或者变量名，进行调用的时候使用的是导入模块里面的，不会和执行文件的方法、变量发生冲突（局部）
import demo
money =100
def read():
    print('out read',money)
demo.read()         # in demo.py   in read 10000

# 5、为啥一个模块不会多次导入
# 因为导入一个模块时会先从sys.modules下面查看是否存在这个模块，存在就不再导入，
# 不存在就依据sys.path路径去寻找模块继续导入
# 然后创建这个模块的命名空间
# 执行文件，把文件中的名字都放到命名空间里
import sys
print(sys.modules.keys())   #dict_keys(['sys', 'builtins', '_frozen_importlib', '_imp', '_thread', '_warnings', '_weakref', 'zipimport', '_frozen_importlib_external', '_io', 'marshal', 'nt', 'winreg', 'encodings', 'codecs', '_codecs', 'encodings.aliases', 'encodings.utf_8', '_signal', '__main__', 'encodings.latin_1', 'io', 'abc', '_abc', 'site', 'os', 'stat', '_stat', 'ntpath', 'genericpath', 'os.path', '_collections_abc', '_sitebuiltins', 'sitecustomize', 'demo'])


# 6、给一个模块起别名
# 应用场景：
# 1、模块名或者方法名太长
# 2、通过别名同时操作相同模块，提高代码的兼容性
# 3、重命名后，之前的模块名不能使用了，只能用重命名的
import time as t
print(t.time())         # 1547781355.3096266

# 用法一：
# 有两中sql模块mysql和oracle，根据用户的输入，选择不同的sql功能
#mysql.py
# def sqlparse():
#     print('from mysql sqlparse')
# #oracle.py
# def sqlparse():
#     print('from oracle sqlparse')

#test.py
db_type=input('>>: ')
if db_type == 'mysql':
    import mysql as db
elif db_type == 'oracle':
    import oracle as db
db.sqlparse()

# 用法二：
# 为已经导入的模块起别名的方式对编写可扩展的代码很有用，假设有两个模块xmlreader.py和csvreader.py，
# 它们都定义了函数read_data(filename):用来从文件中读取一些数据，但采用不同的输入格式。可以编写代码来选择性地挑选读取模块，例如

# f = open('xmlreader.py',mode='w',encoding='utf-8')

# f = open('csvreader.py',mode='w',encoding='utf-8')
file_format = input('>>:')
if file_format == 'xml':
    import xmlreader as db
elif file_format == 'csv':
    import csvreader as db
db.read_data(file_format)

# 7、在一行导入多个模块
import sys,os,time          # 但是不推荐这个导入方式

# 8、模块导入的顺序
# 1、内置模块 sys，os，time，；urllib
# 2、扩展模块 django
# 3、自定义模块

# 9、模块导入from 模块名 import 模块
from time import sleep

from demo import read

import sys
print(sys.path)
# 10、from 模块名 import 模块后使用方式
sleep(10)
read()

# 11、通过from导入的执行文件中存在和导入模块相同的方法变量，调用时会有冲突,使用的是执行文件的read方法（全局）
from demo import read
def read():
    print('out demo read')
read()          # out demo read

# 12、通过from导入方式导入多个变量、方法
from demo import money,read
# print(money)
# read()
money = 200
read()          # in read 10000,这里的money用的还是导入模块的，因为money的内存地址没变

# 13、导入全部(不太安全)
from demo import *      # in demo.py
print(money)             # 10000
read()                   # in read 10000

# 14、双下_all_方法与from demo import * 结合使用用于控制导入后可以使用的变量或者方法(好像3.7后可以用)
from demo import *
print(money)
read()

# 总结：
# 模块不会重复被导入，因为导入的模块从sys.moudles检查是否存在该模块
# 从哪儿导入模块：sys.path
# import 模块名
#     1、调用： 模块名.变量名
#     2、和本文件中的变量名不冲突，使用导入的变量名
#     3、import 模块名 as 重命名模块名：提高代码兼容性的时候使用
#     4、导入多个模块，import 模块1，模块2

# from 模块名 import 方法名
#     1、调用：方法名或者变量
#     2、和本文件中的变量名冲突，使用文件中的变量名
#     3、from 模块名1，模块名2
#     4、from 模块名 import 变量名 as 重命名变量名
#     5、from 模块名 import * ：将模块中的所有变量名都放到内存中
#     6、from 模块名 import * 和_all_是一对，结合使用，没有这个变量则导入所有的，有这个变量名，则只导入all列表中的变量名

# 所有的模块导入尽量往上写
# 模块导入的顺序
    # 内置模块 sys，os，time，；urllib
    # 扩展模块 django
    # 自定义模块
import time