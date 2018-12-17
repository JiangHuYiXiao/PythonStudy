#-*- coding:utf-8 -*-
# re模块下的常用方法:
# 1、findall:返回所有满足正则表达式匹配条件的结果，放在一个列表中
# 格式：
#     import re
#     ret = re.findall('正则表达式','待匹配的字符')
#     print(ret)
'''
import re
ret = re.findall('a','ab')
print(ret)        # ['a']


import re
ret = re.findall('[0-9]','jis22142342ijrew12')
print(ret)

# ['2', '2', '1', '4', '2', '3', '4', '2', '1', '2']

# 2、search:从前往后找，返回第一次查找到的结果返回的结果需要用group接收，如果没有找到返回None，调用group报错
#     格式：import re
#     ret = re.search('正则表达式','待匹配的字符串')
#     res = ret.group()
#     print(res)
import re
ret = re.search('[a-z]','12werww123')
# print(ret)  #<re.Match object; span=(2, 3), match='w'> 返回一个对象
res = ret.group()
print(res)  # w


import re
ret = re.search('[a-z]','12123')
print(ret)  # None
res = ret.group()
print(res)  # 'NoneType' object has no attribute 'group'


# 3、match：从头开始匹配，如果开头匹配上了就返回一个变量，变量需要用group接收，如果开头没有匹配上就返回None
import re
ret = re.match('[0-9]','1abc')
print(ret)  # <re.Match object; span=(0, 1), match='1'>
res = ret.group()
print(res)  # 1

import re
ret = re.match('[0-9]','abc1'/;)
print(ret)  # None
res = ret.group()
print(res)  # 'NoneType' object has no attribute 'group'


# 4、分割split,返回分割后的结果
import re
ret = re.split('[ab]','abcd') # 先按照a分割，得到''和'bcd'，再按照b分割'bcd',得到''和'cd'
print(ret)
'''
# 5、替换sub，返回替换后的结果，将满足正则表达式的都进行替换，原先我们str类型的替换replace只能替换单个
import re
ret = re.sub('[a-z]','A','abaaccddda123ac')
print(ret) # AAAAAAAAAA123AA



