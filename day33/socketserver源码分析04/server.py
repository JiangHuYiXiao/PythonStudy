# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/10/10 8:22
# @Software       : Python_study
# @Python_verison : 3.7
import socketserver
socketserver.ThreadingTCPServer
# 1、继承关系
'''
class ThreadingTCPServer(ThreadingMixIn, TCPServer): pass
class TCPServer(BaseServer):
'''

# 2、各个类的方法：
# ThreadingTCPServer类：
# 无

# ThreadingMixIn类：
'''
def process_request_thread(self, request, client_address):
def process_request(self, request, client_address):
def server_close(self):
'''
# TCPServer类：
'''
def __init__(self, server_address, RequestHandlerClass, bind_and_activate=True):
def server_bind(self):
def server_activate(self):
def server_close(self):
def fileno(self):
def get_request(self):
def shutdown_request(self, request):
def close_request(self, request):


'''
# 3、self对象是TreadingTCPServer的对象

# 总结：
# Python源码学习方法：
# 1、先了解各个类的继承关系
# 2、再了解各个类中的方法
# 3、所有的self的对象必须了解是谁的对象
# 4、所有的方法调用必须退回到最子类中开始查找，逐级往上找