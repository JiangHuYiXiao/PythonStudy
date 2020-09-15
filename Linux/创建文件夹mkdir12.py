# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/9/15 9:15
# @Software       : Python_study
# @Python_verison : 3.7
# 使用mkdir是创建文件夹

# 如果需要在一个文件夹中创建另一个文件夹，再在另一个文件夹里面创建一个其他文件夹
# 可以使用 mkdir /A/B/C/D/E -p命令进行创建
'''
jianghu@ubuntu:~$ mkdir A/B/C/D/E -p
jianghu@ubuntu:~$ ls
11.txt  12.txt  A  demo.python  examples.desktop  公共的  模板  视频  图片  文档  下载  音乐  桌面
jianghu@ubuntu:~$ tree
.
├── 11.txt
├── 12.txt
├── A
│   └── B
│       └── C
│           └── D
│               └── E
├── demo.python
├── examples.desktop
├── 公共的
├── 模板
├── 视频
├── 图片
├── 文档
├── 下载
├── 音乐
└── 桌面'''

