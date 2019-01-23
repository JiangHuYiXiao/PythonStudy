# -*- coding:utf-8 -*-
# 绝对路径导入：
#      包的初识我们讲的都是以绝对路径进行导入的，只要路径发生改变就需用重新更新导入代码

# 相对路径导入：可以随意移动包，只要能找到包的位置，就可以使用包里的模块
import glance
glance.api.policy.get()         # from policy.py

# 就算glance整个文件移动到了新的dir文件也不许更改__init__.py文件的导入方式
# 只需要修改执行文件的导入方式
# from dir import glance
# glance.api.policy.get()