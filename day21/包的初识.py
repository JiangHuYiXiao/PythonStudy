# -*- coding:utf-8 -*-
# 包：就是很多模块的集合
# 包与模块的区别一般是，包他会包含__init__方法（python2.7如果包里面没有init文件是会执行导入的包会报错，python3.0之后不会）

# １、无论是import形式还是from...import形式，凡是在导入语句中（而不是在使用时）遇到带点的，都要第一时间提高警觉：这是关于包才有的导入语法
# 2、包是目录级的（文件夹级），文件夹是用来组成py文件（包的本质就是一个包含__init__.py文件的目录）
# 3、import导入文件时，产生名称空间中的名字来源于文件，import 包，产生的名称空间的名字同样来源于文件，即包下的__init__.py，导入包本质就是在导入该文件

# 强调：
# 　　1、在python3中，即使包下没有__init__.py文件，import 包仍然不会报错，而在python2中，包下一定要有该文件，否则import 包报错
# 　　2、创建包的目的不是为了运行，而是被导入使用，记住，包只是模块的一种形式而已，包即模块
'''
import os
os.makedirs('glance/api')
os.makedirs('glance/cmd')
os.makedirs('glance/db')
l = []
l.append(open('glance/__init__.py','w'))
l.append(open('glance/api/__init__.py','w'))
l.append(open('glance/api/policy.py','w'))
l.append(open('glance/api/versions.py','w'))
l.append(open('glance/cmd/__init__.py','w'))
l.append(open('glance/cmd/manage.py','w'))
l.append(open('glance/db/models.py','w'))
l.append(open('glance/db/__init__.py','w'))
map(lambda f:f.close() ,l)

# 注意事项

# 1.关于包相关的导入语句也分为import和from ... import ...两种，但是无论哪种，无论在什么位置，
# 在导入时都必须遵循一个原则：凡是在导入时带点的，点的左边都必须是一个包，否则非法。可以带有一连串的点，如item.subitem.subsubitem,但都必须遵循这个原则。
# 2.对于导入后，在使用时就没有这种限制了，点的左边可以是包,模块，函数，类(它们都可以用点的方式调用自己的属性)。
# 3.对比import item 和from item import name的应用场景：如果我们想直接使用name那必须使用后者。
# 导入包的方式：
# 1、import
# 导入
import glance.api.policy
# 调用
glance.api.policy.get()         # from policy.py


# 2、from 包名 import 包或者模块
# 导入
from glance import api
from glance.api import policy
# from glance import api.policy   import后面不能有.
#调用
api.policy.get()            # from policy.py

# 3、路径添加
# import sys
# print(sys.path)
# sys.path.insert(0,'F:\\PythonStudy\\day21', 'F:\\PythonStudy\\day21\\api')
'''
# 4、__init__.py
# 导入模块默认是执行.py文件，导入包默认却是执行__init__.py文件
# 不管是哪种方式，只要是第一次导入包或者是包的任何其他部分，
# 都会依次执行包下的__init__.py文件(我们可以在每个包的文件内都打印一行内容来验证一下)，这个文件可以为空，但是也可以存放一些初始化包的代码。
import glance           # 导入就是执行__init__.py文件 ***********
# glance.api.policy.get()         # AttributeError: module 'glance' has no attribute 'api',__init__.py文件中未导入
glance.api.policy.get()         # from policy.py

