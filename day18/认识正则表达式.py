# -*- coding:utf-8 -*-
# 一、正则表达式定义：字符串匹配的一种规则，只能匹配字符串。

# 二、正则表达式的规则：
'''
字符组：[字符组]
在同一个位置上可能出现的各种字符组成的一个字符组，在正则表达式中用[]表示
字符分为很多类，比如数字，字母，标点符号等等。
假如你要求一个位置上只允许数字，那么这个位置上的字符只能是0,1,2...9这10个数之一。
一个字符组，只能匹配一个字符
字符组             带匹配字符          匹配结果         说明
[0123456789]           1                  True           字符组中任意一个字符和带匹配的字符相同都可以视为匹配
[0123456789]           11                 False          一个字符组只能匹配一个字符，但是可以分别匹配到1,1
[0123456789]           a                  False         'a'字符不在字符组中
[0-9]                  2                  True          使用[0-9]表示所有的数字和[0123456789]一样
[a-z]                  a                  True          匹配所有的26个小写字母
[A-Z]                  A                  True          匹配所有的26个大写字母
[A-Za-z0-9]            A1a                True          匹配大写字母，小写字母，数字
'''

# 元字符
# 元字符                           匹配内容
#   .                       匹配除换行符外的任意字符
#   \w                      匹配字母数字下划线
#   \s                      匹配任意的空白符
#   \d                      匹配数字
#   \W                      匹配非字母数字下划线的字符
#   \S                      匹配非空白符
#   \D                      匹配非数字
#   \n                      匹配一个换行符
#   \t                      匹配一个制表符
#   \b                      匹配一个单词的结尾
#   ^                       匹配字符串的开头
#   $                       匹配字符串的结尾
#   a|b                     匹配a或者b
#   ()                      匹配括号内的表达式，也表示一个组
#   [...]                   匹配一个字符组中的字符
#   [^...]                  匹配一个除了字符组中的所有字符


# 量词
# 量词                     用法说明
#  *                    重复0次或者多次
#  +                    重复1次或者多次
#  ?                    重复0次或者1次
#  {n}                  重复n次
#  {n,m}                重复n到m次
#  {n,}                 重复n次或者更多次
import re













