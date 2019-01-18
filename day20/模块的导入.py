# -*- coding:utf-8 -*-
'''
# 1、模块导入
import demo         # 输出结果为 in demo.py

# import 具体做了以下事：

#     1、找到模块
#     2、创建这个模块的命名空间
#     3、把文件中的名字都放到命名空间里面

# 2、模块中方法的调用
demo.read()         # in read

# 3、模块中变量的使用
print(demo.money)

# 4、在执行的文件中存在和导入的模块中相同的方法或者变量名
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
'''
