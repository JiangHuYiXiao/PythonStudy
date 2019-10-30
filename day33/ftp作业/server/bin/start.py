# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/10/29 8:40
# @Software       : server
# @Python_verison : 3.7
import os
import sys
import core.server
import socketserver
from core.server import Mysocket
from conf import setting
# 添加模块导入的搜索路径
sys.path.append(os.path.dirname(os.getcwd()))
if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer((setting.addr), Mysocket)  # 实例化，创建对象
    server.serve_forever()
