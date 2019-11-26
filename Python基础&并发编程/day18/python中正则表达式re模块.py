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

# 5、替换sub，返回替换后的结果，将满足正则表达式的都进行替换，原先我们str类型的替换replace只能替换单个
import re
ret = re.sub('[a-z]','A','abaaccddda123ac')
print(ret) # AAAAAAAAAA123AA

# 替换，返回一个元组替换后的结果，包括替换的次数
res = re.subn('[a-z]','A','abaaccddda123ac')
print(res)  # ('AAAAAAAAAA123AA', 12)


# 6、编译字符串，返回一个编译后的正则表达式对象,用于一个正则表达式会被多次使用
import re
obj = re.compile('\d{3}')
ret = obj.search('abc123def344')
print(ret.group())  # 123,返回第一个123
ret1 = obj.match('abc123def344')
print(ret1.group()) # 'NoneType' object has no attribute 'group'

# 7、返回一个存放匹配结果的迭代器,需要调用group()
import re
ret = re.finditer('[\d]','abc123abdedefag12')
for i in ret:
    print(i.group())    # 1 2 3 1 2
# 或者
print(next(ret).group())    # 1
print(next(ret).group())    # 2
print(next(ret).group())    # 3

# 需求1：写一个身份证的正则表达式:
# 身份证号码是一个长度为15或18个字符的字符串，如果是15位则全部由数字组成，首位不能为0；
# 如果是18位，则前17位全部是数字，末位可能是数字或x
import re
ret = re.findall('^[1-9][0-9]{13,16}[0-9x]$','110101198001017032')  # 15位后面是x也是符合，所以这个正则表达式不够好，16位也是可以匹配，$符号可以加，或者不加
print(ret)
ret = re.findall('^[1-9][0-9]{13,16}[0-9x]$','110101198001017')
print(ret)
ret = re.findall('^[1-9][0-9]{13,16}[0-9x]$','11010119800101x')
print(ret)
ret = re.findall('^([1-9][0-9]{16}[0-9x]|[1-9][0-9]{14})$','110101198001017') # 最好的身份证正则表达式
print(ret)

# 注意：
# 1、search、match的优先级查询：如果正则表达式中有分组,优先使用group()返回没有分组的结果，使用group(1)匹配第一个分组，group(2)匹配第二个分组，以此类推
import re
ret = re.search('^([1-9][0-9]{16})?([0-9x])$','110101198001017032')
print(ret.group())
print(ret.group(1)) # 11010119800101703
print(ret.group(2)) # 2

# 2、findall的优先级查询：如果正则表达式中有分组先匹配分组
import re
ret = re.findall('^([1-9][0-9]{16})?([0-9x])$','110101198001017032')
print(ret)  # [('11010119800101703', '2')]，匹配结果是优先分组

# 取消分组优先，在分组最前面加上?:

import re
ret = re.findall('^(?:[1-9][0-9]{16})?[0-9x]$','110101198001017032')
print(ret)  # ['110101198001017032']，分组优先被取消
'''

# ？号的三种用法在正则表达式中
#     1、量词？,0或者1次
#     2、惰性词*？，放在量词后面
#     3、取消分组？：放在分组前面

# 3、split的优先级查询：split中加上分组，则在进行切割时会保留切割的元素
# 没有使用分组
import re
res = re.split('\d','123a456bcd789')
print(res)  # ['', '', '', 'a', '', '', 'bcd', '', '', '']

# 使用分组
import re
res = re.split('(\d)','123a456bcd789')
print(res)  # ['', '1', '', '2', '', '3', 'a', '4', '', '5', '', '6', 'bcd', '7', '', '8', '', '9', '']