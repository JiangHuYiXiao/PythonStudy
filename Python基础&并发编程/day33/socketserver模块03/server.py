# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/9/25 16:52
# @Software       : Python_study
# @Python_verison : 3.7
# 我们知道启动一个socket的server只能与一个client通信，如果想要启用一个socket时和多个client通信那么我们可以使用socketserver模块。
# socketserver只是在socket上进行了一层封装
import socketserver
# 创建一个自己的类
class Mysocket(socketserver.BaseRequestHandler):        # 继承一个处理基础请求的父类
        def handle(self):           # 必须创建一个handle方法
            while True:
                res = self.request.recv(1024)     # self.request == conn
                print(res.decode('utf-8'))
                info = input('>>>:')
                self.request.send(info.encode('utf-8'))

if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1',9999),Mysocket)      # 实例化，创建对象
    server.serve_forever()