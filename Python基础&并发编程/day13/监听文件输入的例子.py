# -*- coding:utf-8 -*-
#1、 简单的文件监听的例子：

def listener(filename):
    with open(filename,mode = 'r',encoding = 'utf-8') as file:
        while True:
            line = file.readline()
            if line.strip():
                print(line.strip())

listener()


# 2、如果要求前面2行是要加上***，后面的行加上###，这个函数是无法满足的
def listener(filename):
    with open(filename,mode='r',encoding='utf-8') as file:
        while True:
            line = file.readline()
            if line.strip():
                (line.strip())

res = listener('file1')
count = 0
for i in res:

    if count < 2:
        print('***',i)
    else:
        print(i,'###')
    count += 1

# 3、如果文件中行包含有python则打印，做到一个监听过滤的功能
def listener(filename):
    with open(filename,mode='r',encoding='utf-8') as file:
        while True:
            line = file.readline()
            if line.strip():
                yield(line.strip())

res = listener('file1')

for i in res:
    if 'python' in i:
        print(i)
