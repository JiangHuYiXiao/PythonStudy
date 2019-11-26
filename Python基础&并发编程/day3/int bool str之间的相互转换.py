#-*- coding:utf-8 -*-
# int
a = 14
b =a.bit_length()  #表示数据可以用多少个二进制位数来表示
print(b)
c = bin(14)   #二进制位数为：0b1110
print(c)


# bool 只有True 或者 False，常用方法没有

# str 在下一课讲解，这里延伸讲解int、bool、str之间的转换

# 1、int---->bool int为非零则转换成bool值为True，int为零，则转换成bool值则为False
i = 11
b1 = bool(i) #True
print(b1)

# 在实际工作中经常会使用如下语句
# while 1:
#     print('高')   #它的效率高，直接转换成二进制
#
# while True:
#     print('低')   #效率低 ，先转1，再转二进制所以效率低


# 2、bool ---->int
boo11 = False
i1 = int(boo11)
print(i1)  #0

boo12 = True
i2 = int(boo12)
print(i2)  #1

# 3、int---->str
s1 = str(i)
print(s1)  #'11'  int转换成str是没有限制条件的

# 4、str---->int
str1 = '123122423'
i3 = int(str1) #123122423 str转换成int，是有限制条件的，str必须是数字
print(i3)

# str2 ='abc'
# i4 = int(str2) ValueError: invalid literal for int() with base 10: 'abc'
# print(i4)  #

# 5、str---->bool  str为非空则bool值为True，str为空，则bool值为False
bool3 = bool(str1)
print(bool3)

str2 = ''
bool4 = bool(str2)
print(bool4,type(bool4))
# 在实际工作中会这样写
s #前端传到后台为空字符
if s:
     print('你输入的字符串为空')
else:
    print('你输入字符不为空')

# 6、bool---->str
str3 = str(bool4)
print(str3,type(str3))
bool5 = True
str4 = str(bool5)
print(str4,type(str4))