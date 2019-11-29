# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/11/29 13:48
# @Software       : Python_study
# @Python_verison : 3.7

# 使用navicat创建表、插入数据、创建库、编辑表等一系列操作。
# 还可以使用navicat备份导出数据库的结构+数（导入的话必须先新建一个库）

# 可以使用sql语句进入导出导入
# 导出现有数据库数据：在命令窗口执行，在哪个路径下打开命令窗口会导出到哪个路径
    # mysqldump -u用户名 -p密码 数据库名称 >导出文件路径           # 结构+数据
    # mysqldump -u用户名 -p密码 -d 数据库名称 >导出文件路径       # 结构
# 导入现有数据库数据：
    # mysqldump -uroot -p密码  数据库名称 < 文件路径
