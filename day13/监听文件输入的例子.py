# -*- coding:utf-8 -*-
f = open('file',encoding = 'utf-8')
while True:
    line = f.readline()
    if line:
        print(line)
