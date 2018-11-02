#-*- coding:utf-8 -*-
# 1、只读：r

'''
# 绝对路径:从根目录去寻找文件
# 以什么编码方式储存的文件就以编码打开，否则会有乱码
f = open('F:\PythonStudy\day8\文件操作绝对路径',mode = 'r',encoding= 'utf-8')
b = f.read()
print(b)
f.close()


# 相对路径：从当前目录去找文件
f = open('文件操作相对路径', mode = 'r',encoding= 'utf-8')
b = f.read()
print(b)
f.close()

# 需要注意
1、文件编写的是什么编码，打开就应该用什么编码打开，否则会乱码
f = open('F:\PythonStudy\day8\文件编码方式为gb2312.txt',mode= 'r',encoding='utf-8')
b = f.read()
print(b)
f.close()   # UnicodeDecodeError: 'utf-8' codec can't decode byte 0xce in position 0: invalid continuation byte
2、需要注意文件的后缀，是否存在重复的文件后缀名
3、只读只允许读，不能再有多余的任何一步
4、以后我们用的较多的还是使用相对路径去对文件进行操作

f = open('文件操作相对路径',mode= 'r',encoding='utf-8')
b = f.read()
f.write('写一下哈')     # io.UnsupportedOperation: not writable
print(b)
f.close()
'''

# 2、只写:如果文件存在则，先删除原文件，然后再添加
f = open('相对路径',mode= 'w',encoding='utf-8')
b = f.write('写个啥')
print(b)
f.close()