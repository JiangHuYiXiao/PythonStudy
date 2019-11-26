# -*- coding:utf-8 -*-

# 运算符
'''
1、算数运算：
+:加，数字之间可以加，字符串和字符串也可以加。
-:减，只有数字之间可以进行减法运算。
*:乘，数字之间可以相乘，字符串和数字也可以相乘。
/:相除，只有数字可以。
%:取余数，只有数字可以。
//:整除，只有数字可以。
**:
'''
print('jianghu'+ 'jiangxi')
print('jianghu'*4)
print(4 / 3)
print(6 % 5)
print(2 // 3)
print(4 // 2)
print(2**16)

'''
2、比较运算：
>:大于:支持数字和字符
<:小于:支持数字和字符
<=:小于等于
>=:大于等于
==:等于
!=:不等于
<>:不等于

'''
s = 's'
j = 'j'
# 查看字符的Ascii码通过ord()函数
print(ord(s))
print(ord(j))
print(ord('1'))
print(s < j) #False

'''
3、赋值运算
=：简单的赋值
+=：加法赋值
-=：减法赋值
*=：乘法赋值
'''
a = 1
b = 2
a += 1
print(a)
a -= 1
print(a)
b *= 2
print(b)
'''
4、逻辑运算
and :x and y,如果x为True，则返回y，x为 False 则返回x。0就是fasle，其他值就是true，如果x和y都为bool类型，则两个同为真则返回真，只要有一个为false，则返回false。
or:x or y，如果x为True，则返回x，x为 False 则返回y。如果x和y都为bool类型，则只要有一个为false，则返回false，则只要有一个为true，则返回true。
not:真返回假，假返回真。

逻辑运算优先级：
() >not >and >or
'''
# x 和 y都是bool类型
# and
print(1 > 2 and 2 > 3)  #False
print(1 < 2 and 3 > 2)  #True
print(1 < 2 and 2 > 3)  #False

# or
print(1 > 2 or 2 > 3)  #False
print(1 > 2 or 3 > 2)  #True
print(1 < 2 or 2 < 3)  #True

#not
print(not(2 > 3))  #True
# article
'''
1,3>4 or 4<3 and 1==1
2,1 < 2 and 3 < 4 or 1>2 
3,2 > 1 and 3 < 4 or 4 > 5 and 2 < 1
4,1 > 2 and 3 < 4 or 4 > 5 and 2 > 1 or 9 < 8
5,1 > 1 and 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6
6,not 2 > 1 and 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6'''

print('-------------------article----------------')
print(3>4 or 4<3 and 1==1)  #False
print(1 < 2 and 3 < 4 or 1>2) #True
print(2 > 1 and 3 < 4 or 4 > 5 and 2 < 1) #True
print(1 > 2 and 3 < 4 or 4 > 5 and 2 > 1 or 9 < 8)#False
print(1 > 1 and 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6) #False
print(not 2 > 1 and 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6)#False

print('---------x 和 y都是数字------------')
print(1 and 2) #x为真则返回y
print(0 and 1) #x为假则返回x（总结：遇到一个假则返回，否则一直判断下去，直到返回最后一个）
print(1 or 2)  #x为真则返回x
print(0 or 3)  #x为假则返回y（总结：遇到真则返回）

# article
print(1 or 12 or 199 or 200) #1
print(1 and 2 and 4 and 0 and 11 )#0
print(1 and 3 or 4 and 5) #3
print(0 or 4 and 3 or 2)  #3
# 比较运算符优先级高于逻辑运算符 and or not,如果先是比较运算则结果为bool，先算出来是int则结果为int
print(1 > 2 and 2 or 4 and 5 < 4) #0 and 2 or 4 and 0  0 or 0 result = False
print(1 > 2 and 2 or 4 and 5 > 4) #True
print(3 < 1 or 2 and 4) #4
print(2 or 3 > 1 and 4) #2
