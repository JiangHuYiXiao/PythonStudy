# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/9/5 16:22
# @Software       : PythonStudy
# @Python_verison : 3.7
# 一个日志模块，记录用户行为和程序运行过程

# 1、默认配置的格式为日志，意思就是比info级别高的（warning，error，critical）才会输出
# import logging
# logging.debug('debug message')
# logging.info('info message')
# logging.warning('warning message')
# logging.error('errror message')
# logging.critical('critical message')

# WARNING:root:warning message
# ERROR:root:errror message
# CRITICAL:root:critical message


# 2、灵活配置日志级别、日志格式、输出位置,通过basicConfig
# 通过basicConfig，不能解决中文乱码的问题
# 通过basicConfig，不能同时往文件和屏幕上输出
# import logging
# logging.basicConfig(level=logging.ERROR,    # 会输出debug以上的日志级别
#                     format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s',
#                     datefmt= '%Y-%m-%d %H:%M:%S',
#                     filename='test.log',
#                     filemode='a'
#                     )
# try:
#     int(input('请输入：'))
# except ValueError:
#     logging.error('输入的值不是一个数字')
#
# logging.debug('debug message')
# logging.info('info message')
# # logging.warning('warning message')
# # logging.error('error message')
# logging.critical('critical message')

'''
logging.basicConfig()函数中可通过具体参数来更改logging模块默认行为，可用参数有：

filename：用指定的文件名创建FiledHandler，这样日志会被存储在指定的文件中。
filemode：文件打开方式，在指定了filename时使用这个参数，默认值为“a”还可指定为“w”。
format：指定handler使用的日志显示格式。
datefmt：指定日期时间格式。
level：设置rootlogger（后边会讲解具体概念）的日志级别
stream：用指定的stream创建StreamHandler。可以指定输出到sys.stderr,sys.stdout或者文件(f=open(‘test.log’,’w’))，
默认为sys.stderr。若同时列出了filename和stream两个参数，则stream参数会被忽略。

format参数中可能用到的格式化串：
%(name)s Logger的名字
%(levelno)s 数字形式的日志级别
%(levelname)s 文本形式的日志级别
%(pathname)s 调用日志输出函数的模块的完整路径名，可能没有
%(filename)s 调用日志输出函数的模块的文件名
%(module)s 调用日志输出函数的模块名
%(funcName)s 调用日志输出函数的函数名
%(lineno)d 调用日志输出函数的语句所在的代码行
%(created)f 当前时间，用UNIX标准的表示时间的浮 点数表示
%(relativeCreated)d 输出日志信息时的，自Logger创建以 来的毫秒数
%(asctime)s 字符串形式的当前时间。默认格式是 “2003-07-08 16:49:45,896”。逗号后面的是毫秒
%(thread)d 线程ID。可能没有
%(threadName)s 线程名。可能没有
%(process)d 进程ID。可能没有
%(message)s用户输出的消息
'''

# 3、配置logging对象输出日志
