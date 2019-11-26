# -*- coding:utf-8 -*-
# 一、正则表达式
#1、 字符组：[] 表示一个字符
# 2、元字符
# \w：匹配字母数字下划线
# \s：匹配空白字符
# \d：匹配数字
# \W：匹配非字母数字下划线
# \S：匹配非空白字符
# \D：匹配非数字
# \w\W,\s\S,\d\D 分别可以匹配所有的字符
# \b: 匹配一个单词的结尾
# \n：匹配换行符
# \t：匹配制表符
# ^: 以什么开头
# $: 以什么结尾
# a|b：a或者b，一直找，找到了就停止

# ():分组，匹配括号内的表达式，用于一个字符整体约束的时候用的

#3、 量词
# *：0到无穷大
# +：1到无穷大
# ？：0或1次
# {n}：匹配n次
# {n,}：匹配n次，到无穷大
# {n,m}：匹配n到m次

# 4、贪婪匹配：默认量词都是贪婪匹配（*，+，？）尽量多的匹配

# 5、惰性匹配：如果想让贪婪匹配变成尽量少的匹配，则需要在量词后面加上?,如：*?,+?

# 6、转义符\
# 正则表达式中，想表达特殊字符的原有意思，而不是正则表达式的意思，可以加上\
# re中，我们可以在字符前面加上r，在正则表达式中也加上r

# 7、flag
# 我们常用的为re.S,在后面加上后，表示.可以代表任意字符

# 二、re模块
import re

# 1、re.findall()    # 查找所有，返回一个列表
# 存在一个分组优先的情况
ret = re.findall('^([1-9][0-9]{16})[0-9x]|[1-9][0-9]{14}$','110101198001017032')
print(ret)      # ['11010119800101703']
# 取消分组优先在分组之前使用?:
ret = re.findall('(?:^[1-9][0-9]{16})[0-9x]|[1-9][0-9]{14}$','110101198001017032')
print(ret)      # ['110101198001017032']

ret = re.findall('.','1101011980010 17 032',re.S)       # 表示.可以匹配任意字符
print(ret)

# 2、re.search()   # 匹配到第一个就返回，需要使用group()
# 匹配不到就返回None
# 使用group(1),表示返回第一个分组，group(2)返回第二个分组
# 还可以给分组加上名字这样在取分组时，可以直接使用名字去取?P<name>
ret = re.search('(\d)(g)','12324gsdfsiwe3223',re.S)
print(ret.group())      # 4g
print(ret.group(1))      # 4
print(ret.group(2))      # g
ret = re.search('(\d)(?P<name>g)','12324gsdfsiwe3223',re.S)
print(ret.group('name'))


# 3、re.match()   # 从头开始匹配，需要使用group()获取值，
# 没有匹配到就返回None
# 取分组内容：
#     1、使用group(1)
#     2、给分组命名?P<name>

ret = re.match('(\d)(a)','1a2324gsdfsiwe3223')
print(ret.group())      # 1a
print(ret.group(1))      # 1
print(ret.group(2))      # a

ret = re.match('(\d)(?P<name1>a)','1a2324gsdfsiwe3223')
print(ret.group('name1'))


# 4、re.split()      # 拆分
# 没有分组
ret = re.split('a','abcdb132asdfg')
print(ret)      # ['', 'bcdb132', 'sdfg']

#有分组
ret = re.split('(a)','abcdb132asdfg')
print(ret)      # ['', 'a', 'bcdb132', 'a', 'sdfg'] 有分组，先按照分组a拆分,被拆的还会保留

# 取消分组
ret = re.split('(?:a)','abcdb132asdfg')
print(ret)      # ['', 'bcdb132', 'sdfg'] 有分组，先按照分组a拆分

# 5、re.sub()替换
ret = re.sub('\w','P','123abc__456')
print(ret)      # PPPPPPPPPPP



# 6、re.subn()替换，返回一个元组，但是会返回替换的次数
ret = re.subn('\w','A','123abc__456')
print(ret)      # ('AAAAAAAAAAA', 11)




# 7、re.finditer() 返回一个正则迭代器，当返回的结果很多需要一个个取时，使用,需要使用group()
ret = re.finditer('\d','123abc456')
# 使用for循环获取
# for i in ret:
#     print(i.group())

# 或者使用next获取
print(next(ret).group())
print(next(ret).group())
print(next(ret).group())
print(next(ret).group())
print(next(ret).group())
print(next(ret).group())

# 8、编译，用于正则表达式长且多次使用
ret = re.compile('\d')
res = re.findall(ret,'123abc456')
# 或者这样
res = ret.findall('123abc456')
print(res)