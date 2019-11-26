# -*- coding:utf-8 -*-
# 1、绝对路径导入：
#      包的初识我们讲的都是以绝对路径进行导入的，只要路径发生改变就需用重新更新导入代码

# 2、相对路径导入：可以随意移动包，只要能找到包的位置，就可以使用包里的模块
import glance
glance.api.policy.get()         # from policy.py

# 就算glance整个文件移动到了新的dir文件也不许更改__init__.py文件的导入方式
# 只需要修改执行文件的导入方式
# from dir import glance
# glance.api.policy.get()

# 3、导入包中所有 from glance.api import * 和__all__一起使用
# 使用：
from glance.api import *
policy.get()


# 4、软件开发规范
# 目录结构一般如下：
'''soft
    bin         # 开始文件
        start.py
        ...
    conf        # 配置文件
        setting.py
        ...
    core        # 核心代码
        core.py
        ...
    db          # 数据库
        alex.json
        ...
    lib         # 自己写的通用模块或者包
        read.py
        ...
    log         # 日志
        server.log
        ...    
    
'''