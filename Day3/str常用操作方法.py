#-*- coding:utf-8 -*-
# 1、字符串首字母大写，其余字母小写
s = 'aBCDerufreoh'
s1 = s.capitalize()
print(s1)

# 2、字符串全部字符大写
s2 = s.upper()
print(s2)
# 举例：
# 登录，输入验证码，不区分大小写
mark = 'sTRobc'
input_Mark = input('请输入验证码:')
if mark.upper() == input_Mark.upper():
    print('通过验证')
else:
    print('验证码错误，请重新输入')

# 3、字符串全部字符小写
s3 = s.lower()
print(s3)

# 4、判断字符串是否全部为字母
s4 = s.isalpha()
print(s4)

# 5、判断字符串是否为数字和字母中的任意组合
s5 = s.isalnum()
print(s5)

# 6、判断字符串是否全部为十进制的数字
s6 = s.isdecimal()
print(s6)

# 7、大写转换为小写，小写转换为大写
s7 = s.swapcase()
print(s7)

# 8、查找字符在字符串的第一次出现位置的索引
s8 = s.find('e')
s9 = s.find('1')  #不存在返回-1
print(s8,s9)

# 9、返回查找字符串的第一次出现位置的索引
s10 = s.index('e')
print(s10)
# s11 = s.index('1')
# print(s11)            #不存在报错：ValueError: substring not found

# 10、替换
s12 = s.replace('e','E')
s13 = s.replace('e','E',1)  #表示只替换一个
print(s12)
print(s13)

# 11、默认去前后空格，可以指定去除前后特定字符串
ss = '  jianghuyixiao   '
s14 = ss.strip()
print(s14)

str1 = '#jianghuyixiao@'
s15 = str1.strip('#')
print(s15)

str2 = ' 1@#$jianghuyixiao@# $ '
s16 = str2.strip('1@ #$')
print(s16)

str3 = '@w#$jianghuyixiao@#$'
s17 = str3.strip('@#$')
print(s17)   #w#$jianghuyixiao  因为w不包含在里面，所以后面的都不删除

# 12、删除右边的空格或者特定字符
str4 = ' @#jianghuyixiao#@@     '
s18 = str4.rstrip(' @#')
print(s18)    #result: @#jianghuyixiao

# 13、删除左边的空格或者特定字符
str5 = ' %%jianghuyixiao&&&^%$$    '
s19 = str5.strip('% ')
print(s19)    #result:jianghuyixiao&&&^%$$

# 举例：一般我们在用户输入的时候难免会输入空格，这个时候就需要我们使用strip进行去除空格
name = input('请输入你的姓名：')
if name.strip() == '江湖':
    print('恭喜用户名输入正确')
else:
    print('用户名不正确')


# 14、format格式化输出的三种方式{}
str6 = '我叫{},我的性别是{},我的年龄是{},再说一次我叫{}'.format('江湖','男','27','江湖')
print(str6)

str7 = '我叫{0},我的性别是{1},我的年龄是{2},再说一次我叫{0}'.format('江湖','男','27')
print(str7)

name = input('请输入你的姓名：')
str9 = '我叫{0},我的性别是{1},我的年龄是{2},再说一次我叫{0}'.format(name,'男','27')
print(str9)

str8 = '我叫{name},我的性别是{sex},我的年龄是{age},再说一次我叫{name}'.format(age = 27,name = 'jianghu',sex = '男')
print(str8)

# 15、统计次数
str10 = 'jianghuayixao'
s20 = str10.count('a')
print(s20)

str11 = 'jianghuayixaoabac'
s21 = str11.count('a',0,8)
print(s21)

s22 = str11.count('an')
print(s22)

# 16、split，字符串转换成列表,默认按照空格拆分(一分为二)
# 这是一个将str转换成列表

str12 = 'jianghu jiangxi jiangsong jiangjiang'
s23 = str12.split()
print(s23)

s24 = str12.split('jiang')
print(s24)  #  ['', 'hu ', 'xi ', 'song ', '', '']

# 17、以空格或者特殊字符分开的首字母大写
str13 = 'jianghu jiangxi jiang'
s25 = str13.title()
print(s25)

str14 = 'jianghu#jiangxi%jiang'
s26 = str14.title()
print(s26)

# 18、字符串是否以什么开头，返回值为布尔值
str15 = 'jianghuyixiao'
s27 = str15.startswith('jiang')
print(s27)

# 19、字符串是否以什么结尾，返回值为布尔值
str16 = 'jianghuyixiaoHH'
s28 = str16.endswith('HH')
print(s28)

# 20、居中处理，并且可以设置字符串长度,不够的话补充空格
str17 = 'jianghu'
s29 = str17.center(20)
print(s29)     #      jianghu