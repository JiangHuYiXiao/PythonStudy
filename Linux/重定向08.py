# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/9/14 9:20
# @Software       : Python_study
# @Python_verison : 3.7
# 所谓重定向就是把一个地方的数据输出到另一个地方查看

# 1、> 如果文件不存在则，新建文件然后把数据添加到改文件，如果文件存在则先删除，后添加
    # jianghu@ubuntu:~$ ls >demo.python
    # jianghu@ubuntu:~$ cat demo.python
    # 11.txt
    # demo.python
    # examples.desktop
    # 公共的
    # 模板
    # 视频
    # 图片
    # 文档
    # 下载
    # 音乐
    # 桌面


# 1、>> 如果文件不存在则，新建文件然后把数据添加到改文件，如果文件存在则直接添加
# jianghu@ubuntu:~$ ls >>demo.python
# jianghu@ubuntu:~$ gedit demo.python
# 11.txt
# demo.python
# examples.desktop
# 公共的
# 模板
# 视频
# 图片
# 文档
# 下载
# 音乐
# 桌面
# 11.txt
# demo.python
# examples.desktop
# 公共的
# 模板
# 视频
# 图片
# 文档
# 下载
# 音乐
# 桌面