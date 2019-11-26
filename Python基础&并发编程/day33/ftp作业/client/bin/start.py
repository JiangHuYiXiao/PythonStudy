# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/10/29 8:42
# @Software       : client
# @Python_verison : 3.7
import os
import sys
from core import client
# 添加模块导入的搜索路径
sys.path.append(os.path.dirname(os.getcwd()))
if __name__ == '__main__':
    client.main()