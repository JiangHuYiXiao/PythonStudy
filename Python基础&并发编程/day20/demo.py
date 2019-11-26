# -*- coding:utf-8 -*-
# _all_ = ['read']    # 只有money变量可以使用
print('in demo.py')
money = 10000
def read():
    print('in read',money)

if __name__ == '__main__':
    print('run the demo')
print(__name__)         #__main__
