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
# 这里内部通过open进行了将str到bytes数据类型然后再bytes到str数据类型的转换，才可以让我们读懂


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


# rb
# f = open('文件操作相对路径', mode = 'rb')
# b = f.read()
# print(b)                     # b'\xe5\x86\x99\xe4\xb8\xaa\xe5\x95\xa5'
# f.close()
#

# 2、只写  如果文件存在内容，则先删除原文件，然后再添加
# w
# f = open('文件操作相对路径',mode= 'w',encoding='utf-8')
# b = f.write('写个啥')  #返回字符数
# print(b)
# f.close()

# wb 以bytes数据类型进行写，wb，因为bytes数据类型的编码方式为utf-8或者gbk等，所以不要写enconding
# f = open('文件操作相对路径',mode= 'wb')
# b = f.write('dfe'.encode('GBK'))  #bytes数据类型转换到str需要经过encode进行编码，unicode转到utf-8或者GBK
# print(b)
# f.close()
'''

# 3、追加 a
f = open('文件操作相对路径',mode= 'a' ,encoding='utf-8')
f.write('追加')
print(f.write)
f.close()

# ab
f = open('文件操作相对路径',mode= 'ab')
f.write('追加'.encode('utf-8'))
print(f.write)
f.close()
