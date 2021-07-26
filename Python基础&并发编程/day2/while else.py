# -*- coding:utf-8 -*-
'''
while 条件：
    循环体
    终止循环
else：
while
else  解释：当循环体中没有被break打断则会运行else，打断则不会运行else
'''
# 例子
a = 0
while a < 5:
    print(a)
    a += 1
    # break
else:
    print('循环结束')  # 0
