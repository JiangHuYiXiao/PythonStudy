# -*- coding:utf-8 -*-
# 今天的作业:计算器
# 去掉所有的空格
# 先算括号里的乘除，再算括号里的加减
# 从括号里取值 == 正则表达式
import re
a = '1 - 2 * ( ( 6 0 -3 0  +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
a1 = a.replace(' ','')
print(a1)
ret = re.findall('','a1')
print(ret)

