#-*- coding:utf-8 -*-
# 1、有变量 name = 'aleX leNb',完成如下操作

name = 'aleX leNb'
# 1)移除name变量对应的值两边的空格，并输出处理结果
name1 = name.strip()
print(name)

# 2)移除name变量左边的'al'，并输出处理结果
name2 = name.lstrip('al')
print(name2)

# 3)移除name变量右边的'Nb'，并输出处理结果
name3 = name.rstrip('Nb')
print(name3)

# 4)移除name变量开头的a和最后的b，并输出处理结果
name4 = name.strip('ab')
print(name4)

# 5)判断变量name是否以al开头，并输出处理结果
name5 = name.startswith('al')
print(name5)

# 6)判断变量name是否以Nb结尾，并输出处理结果
name6 = name.endswith('Nb')
print(name6)

# 7)将name变量对应值中的所有的l替换成p，并输出处理结果
name7 = name.replace('l','p')
print(name7)

# 8)将name变量对应值中的第一个的‘l’替换成‘p’，并输出处理结果
name8 = name.replace('l','p',1)
print(name8)

# 9)将name变量对应值根据所有的‘l’进行分割，并输出处理结果
name9 = name.split('l')
print(name9)  #['a', 'eX ', 'eNb']

# 10)将name变量对应值根据第一个的‘l’进行分割，并输出处理结果
name10 = name.split('l',1)
print(name10)

# 11)将name变量的值变成大写，并输出结果
name11 = name.upper()
print(name11)

# 12)将name变量的值变成小写，并输出结果
name12 = name.lower()
print(name12)

# 13)将name变量的首字母‘a’大写，并输出结果
name13 = name.capitalize()
print(name13)

# 14)判断name变量的‘l’出现几次，并输出结果
name14 = name.count('l')
print(name14)

# 15)判断name变量对应的值的前四位‘l’出现几次，并输出结果
name15 = name.count('l',4)
print(name15)

# 16)从name变量对应的值中找'N',如果找不到则报错，并输出结果
name16 = name.index('N')
print(name16)

# name17 = name.index('n')
# print(name17)  #ValueError: substring not found

# 17)从name变量对应的值中找'N',如果找不到则返回-1，并输出结果
name18 = name.find('N')
print(name18)

name19 = name.find('n')
print(name19)   #-1

# 18)从name变量对应的值中找到'X le'对应的索引，并输出结果
name20 = name.index('X le')
print(name20)

# 19)请输出name变量对应的值的第2个字符
print(name[1])

# 20)请输出name变量对应的值的前3个字符
print(name[0:3])

# 21)请输出name变量对应的值的后2个字符
print(name[-2:])

# 22)请输出name变量对应的值中‘e’所在的索引位置
print(name.index('e'))

# 22)获取子序列，去掉最后一个字符，如‘oldboy’--->'oldbo'
# 方法1：
oldboy = 'oldboy'
name21 = oldboy.rstrip('y')
print(name21)
# 方法2：
print(oldboy[:-1])
print(oldboy)   #字符串的所有操作都是在新的字符串上操作，旧的字符串上不操作


# 2、有字符串 s = '132a4b5c'

# 1)通过对li列表切片形成新的字符串，s1 = '123

# 方法1
s = '132a4b5c'
ss = s.replace('32','23')
print(ss)
li = ss[0:3]
print(li)

# 方法2
li = s.strip('4b5c').replace('32','23')[0:3]
print(li)

# 方法3
li = s[0]+s[2]+s[1]
print(li)

# 方法4
li = s[s.index('1')]+s[s.index('2')]+s[s.index('3')]
print(li)

# 2)通过对li列表切片形成新的字符串，s2 = 'a4b'
s2 = s[3:6]
print(s2)

# 3)通过对li列表切片形成新的字符串，s3 = '1245'
s3 = s.replace('32a4b5c','245')
print(s3)

# 4)通过对li列表切片形成新的字符串，s4 = '3ab'
s4 = s[1:6:2]
print(s4)

# 5)通过对li列表切片形成新的字符串，s5 = 'c'
s5 = s[-1]
print(s5)

# 6)通过对li列表切片形成新的字符串，s5 = 'ba3'
s = '132a4b5c'
s6 = s[5:0:-2]
print(s6)


# 3、使用while和for循环分别打印‘asdfer’中每个元素

str1 = 'asdfer'
for i in str1:
    print(i)

index = 0
str_index = len(str1)
while index < str_index:
    print(str1[index])
    index += 1


# 4、实现一个整数加法计算器（如：content = input('请输入内容:')如：用户输入5+9或者5 +9或者5+ 9然后进行分割再进行计算）

num = input('请输入内容:')
list = num.strip().split('+')
sum = 0
for i in list:
    print(i)
    sum = sum + int(i)
print(sum)

# 5、计算用户输入的内容中有几个整数（如：content = input('请输入内容:')如：’fssdfsddfs646de23wrwer099dsret‘）
sum = 0
content = input('请输入内容:')
for i in content:
    if i.isdecimal():
      sum += 1
print(sum)

# 6、分别用for和while循环输出字符串 s = input('请输入内容：')的每一个字符。
s = input('请输入你想输入的内容：')
for i in s:
    print(i)

i = 0
while i < len(s):
    print(s[i])
    i += 1

