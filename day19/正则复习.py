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
