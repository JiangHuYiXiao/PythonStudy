# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/10/30 9:31
# @Software       : server
# @Python_verison : 3.7
import json
# 我们知道启动一个socket的server只能与一个client通信，如果想要启用一个socket时和多个client通信那么我们可以使用socketserver模块。
# socketserver只是在socket上进行了一层封装
import socketserver
# 创建一个自己的类
from core import views
from conf import setting
class Mysocket(socketserver.BaseRequestHandler):        # 继承一个处理基础请求的父类
        def handle(self):           # 必须创建一个handle方法
            msg = self.myrecv()
            # 消息的转发，把任务转给view文件中的对应的方法
            # {'username','password','operation'}
            op_str = msg['operation']
            if hasattr(views,op_str):
                func = getattr(views,op_str)
                ret = func(msg)
                self.my_send(ret)


        def myrecv(self):           # 派生方法
            msg = self.request.recv(1024)
            msg = msg.decode('utf-8')
            msg = json.loads(msg)
            return msg
        def my_send(self,msg):
            json.dumps(msg).encode(setting.code)
            self.request.send(msg)
