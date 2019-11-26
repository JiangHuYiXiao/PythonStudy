# -*- coding:utf-8 -*-
# 1、匹配标签
'''
# 方法1：
import re
ret = re.search('<(?P<tag_name>\w+)>\w+</(?P=tag_name)>','<h1>hello</h1>')
#还可以在分组中利用?<name>的形式给分组起名字
#获取的匹配结果可以直接用group('名字')拿到对应的值
print(ret.group('tag_name'))  #结果 ：h1
print(ret.group())  #结果 ：<h1>hello</h1>

# 方法2：
ret = re.search(r"<(\w+)>\w+</\1>","<h1>hello</h1>")
#如果不给分组起名字，也可以用\序号来找到对应的组，表示要找的内容和前面的组内容一致
#获取的匹配结果可以直接用group(序号)拿到对应的值
print(ret.group(1))
print(ret.group())  #结果 ：<h1>hello</h1>

# 2、匹配整数

# 方法1：
import re
ret=re.findall(r"\d+","1-2*(60+(-40.35/5)-(-4*3))")
print(ret) # ['1', '2', '60', '40', '35', '5', '4', '3'] 这个不够全面，把负数也匹配到了，把小数也匹配到了

ret = re.findall(r'\d+\.\d+|\d+','1-2*(60+(-40.35/5)-(-4*3))')
print(ret)  # ['1', '2', '60', '40.35', '5', '4', '3']  这可以匹配到小数和负数

ret = re.findall(r'\d+\.\d+|(\d+)','1-2*(60+(-40.35/5)-(-4*3))') # 给加上分组，分组优先
print(ret)      # ['1', '2', '60', '', '5', '4', '3'] 会有空字符

ret = re.findall(r'\d+\.\d+|(\d+)','1-2*(60+(-40.35/5)-(-4*3))') # 给加上分组，分组优先
ret.remove("")      # 把空字符删除
print(ret)      # ['1', '2', '60', '5', '4', '3']

# 如果想让特殊字符-、.、*、+、（）表示原有意思，我们可以在正则表达式前面加上r



# 3、数字匹配
# 1、 匹配一段文本中的每行的邮箱
# http://blog.csdn.net/make164492212/article/details/51656638
import re
with open('email',mode='r+',encoding='utf-8')as file:
    line = file.readlines()
for i in line:
    # print(i)
    ret = re.findall('[-\w]+@[-\w]+\.[a-zA-Z]+',i)
    # \w[-\w. +] * @ ([A - Za - z0 - 9][-A - Za - z0 - 9] +\.) + [A - Za - z]{2, 14}   这个也可以
    print(ret)

# 2、 匹配一段文本中的每行的时间字符串，比如：‘1990-07-12’；
import re
with open('正则练习文本',mode='r+',encoding='utf-8') as file:
    line = file.readlines()
for i in line:
    ret = re.findall('[1-9]\d{3}-[0-1][0-9]-[0-3]\d',i)
    print(ret)

#    分别取出1年的12个月（^(0?[1-9]|1[0-2])$）、
#    一个月的31天：^((0?[1-9])|((1|2)[0-9])|30|31)$
#
# 3、 匹配qq号。(腾讯QQ号从10000开始)
import re
with open('正则练习文本',mode='r+',encoding='utf-8') as file:
    line = file.readlines()
for i in line:
    ret = re.findall('[1-9](\d{4,})',i)
    print(ret)
'''
# 4、 匹配一个浮点数。       ^(-?\d+)(\.\d+)?$   或者  -?\d+\.?\d*
import re
ret = re.findall('-?\d+\.\d*','-12.23')
print(ret)
ret = re.findall('-?\d+\.\d*','12.23')
print(ret)
# 5、 匹配汉字。             ^[\u4e00-\u9fa5]{0,}$
ret = re.findall('[\u4e00-\u9fa5]+','WOD我的')
print(ret)
# 6、 匹配出所有整数