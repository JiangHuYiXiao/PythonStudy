#-*- coding:utf-8 -*-
# sys模块是一个与python解释器相关的模块
'''
import sys
# 1、platform，返回操作系统平台名称
print(sys.platform)         # win32

# 2、version     返回python解释器的版本
print(sys.version)      #   3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)]

# 3、exit 退出程序，可以传参数exit(0)正常退出,exit(1)错误退出
# print(sys.platform)
# exit(0)
# print(sys.version)
# exit(1)

# 4、path  返回模块搜索路径，先去找该文件的路径，再去找改文件上一级，再去找python解释器的目录，
print()
# ['F:\\PythonStudy\\day19', 'F:\\PythonStudy',
# 'C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python37\\python37.zip',
#  'C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python37\\DLLs',
#  'C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python37\\lib',
# 'C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python37',
# 'C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python37\\lib\\site-packages',
# 'F:\\Pycharm\\PyCharm 2018.2.2\\helpers\\pycharm_matplotlib_backend']
'''
# 5、argv 返回一个命令行参数的list，第一个元素是程序本身的路径,一般python脚本拿过来不一定是在pycharm上执行，都是拿过来在终端执行
# 然后有的时候还需要在执行时传递参数，这个时候就可用argv
# 使用argv时需要在terminal进行调用，都是在命令窗口
import sys
ret = sys.argv
print(ret)      # ['sys模块.py']
name = ret[1]
password = ret[2]
if name == 'jianghu' and password == '123456':
    print('登录成功')
else:
    print('错误的账号或者密码')
    exit(0)
print('你可以使用系统了')
