# -*- coding:utf-8 -*-

'''
py2，和py3通用的编码方式：

编码回顾：
ASCII码，只有英文，不支持中文，A = 1bit = 8byte  0001101

Unicode：
支持所有国家的语言，
英文：用4个字节表示一个英文， A = 4bit = 32byte   0001001 0001001 0000000 11101010
中文：用4个字节表示一个中文， 中 = 4bit = 32byte  001001 0000001 0000000 11101010

utf-8：
是对unicode编码的优化，
英文：用一个字节表示为一个英文， A = 1bit = 8byte   0000000
中文：用3个字节表示一个中文，中 = 3bit = 24byte     1000000 0001000 0000001

gbk：
英文：用一个字节表示为一个英文， A = 1bit = 8byte    1000000
中文：用2个字节表示为一个英文， 中 = 2bit = 16byte   1000001 1000000

# 1、各个编码之间的二进制，不能识别，会产生乱码
# 2、我们文件的储存（硬盘）和传输不能是unicode因为容量太大，只能是utf-8，gbk，gb2312，ascii
'''
# py3
# str在内存中是用unicode进行编码的
# py3中存在一个特殊的数据类型，bytes类型，
# 他和str差不多，但是他在内存中的的编码方式是（utf-8，gbk，gb2312，ascii）
# 所以我们存储和传输应该是将str的unicode转换成bytes

# 内存中str和bytes存储中英文的区别
# 英文：
a = 'jianghu'
# 1、str:
# 表现形式：a = 'jianghu'
# 编码方式：unicode
print(a.encode('utf-8'))  #b'jianghu'    #encode是将字符串a，转换成bytes，然后以utf-8进行编码

# 2、bytes:
# 表现形式：a = b'jianghu'
# 编码方式：utf-8或者GBK,gb2312，ascii

# 中文：
a1 = '江湖'
# 1、str:
# 表现形式：a = '江湖'
# 编码方式：unicode

# 2、bytes:
# 表现形式：a = b'\xe6\xb1\x9f\xe6\xb9\x96'
# 编码方式：utf-8或者GBK,gb2312，ascii
b = a1.encode('utf-8')   #encode是将字符串a1，转换成bytes，然后以utf-8进行编码
print(b)   # b'\xe6\xb1\x9f\xe6\xb9\x96'

# 为啥我们不用bytes表现字符串，且bytes的编码方式（utf-8,gbk等）都可以直接在硬盘上存储，和进行传输？，
# 那是因为bytes的表现形式，为16进制，我们不好识别