# -*- coding:utf-8 -*-

# 1、read和seek的区别
'''
# read
# 字母
f = open('文件操作功能(字母)',mode='r+',encoding='utf-8')
re = f.read(2)   #读：是按照字符：（就是该字符串的最小单元）
print(re)   #we
f.close()

# 中文
f = open('文件操作功能(中文)',mode='r+',encoding='utf-8')
re = f.read(2)   #读：是按照字符：（就是该字符串的最小单元）
print(re)           #文件
f.close()

f = open('文件操作功能(中文)',mode='r+',encoding='utf-8')
re = f.read(3)   #读：是按照字符：（就是该字符串的最小单元）
print(re)       #文件操
f.close()

# seek
f = open('文件操作功能(中文)',mode='r+',encoding='utf-8')
f.seek(3)        #光标按照字节，进行移动光标，移动到第一个字符之后
re = f.read(3)   #读：是按照字符：（就是该字符串的最小单元）
print(re)       #件操作
f.close()

f = open('文件操作功能(中文)',mode='r+',encoding='utf-8')
f.seek(2)        #光标：按照字节，进行移动光标，移动到第一个字符之后
re = f.read(3)   #读：是按照字符：（就是该字符串的最小单元）
print(re)       #报错，解码出错，因为一个中文在utf-8中是要按照三个字节表示
f.close()
'''
# 2、tell：告诉你光标的位置
'''f = open('文件操作功能(中文)',mode='r+',encoding='utf-8')
# print(f.tell())  #先查看光标的位置，然后再通过seek进行调动光标的位置
# f.seek(3)        #光标按照字节，进行移动光标，移动到第一个字符之后
# print(f.tell())
# re = f.read(3)   #读：是按照字符：（就是该字符串的最小单元）
# print(re)       #件操作
# f.close()

f = open('文件操作功能(中文)',mode='a+',encoding='utf-8')
print(f.tell())            #先查看光标的位置，然后再通过seek进行调动光标的位置
f.seek(f.tell()-3)        #读取后三个字节的字
print(f.tell())
re = f.read()   #读：光标从21到最后24
print(re)       #文
f.close()
'''
# 3、其他功能
# f.readable  是否可读，返回布尔值
# f = open('文件操作功能(中文)',mode='r+',encoding='utf-8')
# f.readable()  #
# print(f.readable())   #
# f.close()

# f.readline  :一行一行读
# f = open('文件操作功能(中文)',mode='r+',encoding='utf-8')
# line1 = f.readline()
# line2 = f.readline()
# print(line1,line2)

# 每一行，读出来当做列表的一个元素
# f = open('文件操作功能(中文)',mode='r+',encoding='utf-8')
# line1 = f.readlines()
# print(line1)              #['文件操作功能中文，附近的人，我去，你去，大家去\n', '第二行\n', '第三行\n']

# for i in f.readlines():
#     print(i)
# 这样可以for循环文件取出整个文件
# for i in f:
#     print(i)

# f.truncate()截取文件内容,必须是可写的模式下进行，默认为空
# f = open('文件操作功能(中文)',mode='r+',encoding='utf-8')
# tr = f.truncate()  #返回整个文件的所有字节
# print(tr)


# f = open('文件操作功能(中文)',mode='r+',encoding='utf-8')
# tr = f.truncate(3)  #返回是字节，源文件只剩下一个‘第’
# print(tr)

# 另一种文件操作的方法

# with open('文件操作功能(中文)',mode='r+',encoding='utf-8') as file: #不需要写file.close
#     print(file.read())


# with open('文件操作功能(中文)',mode='r+',encoding='utf-8') as file,\
#         open('文件操作功能(字母)',mode='r+',encoding='utf-8') as file1: #不需要写file.close
#     print(file.read())
#     print(file1.read())

# 文件修改
# OS模块简单的来说它是一个Python的系统编程的操作模块，可以处理文件和目录这些我们日常手动需要做的操作。
# 将硬盘存放的该文件的内容全部加载到内存，在内存中是可以修改的，修改完毕后，再由内存覆盖到硬盘（word，vim，nodpad++等编辑器）

import os
with open('AL',mode='w+',encoding='utf-8') as read_file,open('SB',mode='w+',encoding='utf-8') as write_file:
    data = read_file.read()
    data = data.replace('AL','SB')
    write_file.write(data)
os.remove('AL')
os.rename('SB','AL')

