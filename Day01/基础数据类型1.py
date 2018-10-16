# -*- coding:utf-8 -*-
# 1、数字（int）
a = 2
b = 8
c = a + b
print(a,b,c)
# 通过type()方法可以查看变量属于哪种的数据类型
print(a,type(a))
d = 3.4
# float
print(d,type(d))
# 运算:+ ,-,*,/,%
print(b - a)
print(b * a)
print(b / a)
print(b % a)

# 2、字符串（str）
name = 'jianghu'
print(name,type(name))
# 字符串不能相减、除，但是支持+和*
sex = '男'
print(name + sex)
print(name * 8)
'''
注意：
多行字符串需要使用三个单引号或者三个双引号
已经存在单引号后，只能使用双引号
'''
msg = '''
人生苦短
我要学python
努力
'''
print(msg)
info = "i'm 18 old"
print(info)
# str转换成int通过int函数，但是有个条件是参数必须是数字
str11 = int(11)


# 3、布尔类型bool
print(True,type(True))