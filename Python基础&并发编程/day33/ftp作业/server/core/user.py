# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/10/30 15:34
# @Software       : server
# @Python_verison : 3.7
import os
from conf import setting
class User:
    def __init__(self,name):
        self.name = name
        self.home = os.path.join(setting.home_path,name)
        self.cur_path = self.home
        self.disk_space = setting.space   # 字节，2G
        self.file_size = 0
        