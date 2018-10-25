# -*- coding:utf-8 -*-

# -*- coding:utf-8 -*-
ascii = input('请输入十进制的数字：')
print(ascii,'的ACSII码为:',chr(int(ascii)))
dec = input('请输入ASCII码：')
print(dec,'的十进制为：',ord(dec))

for i in range(0,128):
    print(i,'的ACSII码为:', chr(i))