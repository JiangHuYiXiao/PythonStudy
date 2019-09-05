# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/9/5 9:50
# @Software       : PythonStudy
# @Python_verison : 3.7

# 作业，比较两个文件是否一致
import hashlib
import os
def file_md5(path):
    '''
    文件校验
    :param path: path 文件路径
    :return: 返回加密文件
    '''
    path_size = os.path.getsize(path)
    md5_object = hashlib.md5()
    with open(path,mode='rb')as f:
        while path_size >=4096:
            cont = f.read(4096)
            md5_object.update(cont)
            path_size = path_size - 4096
        else:
            cont = f.read()
            if cont:
                md5_object.update(cont)
    return md5_object.hexdigest()

def jy(path1,path2):
    '''
    文件传输校验
    :param path1: 文件1
    :param path2: 文件2
    :return: 是否一致
    '''
    if file_md5(path1) == file_md5(path2):
        return '文件一致'
    else:
        return  '文件不一致'
path1 = r'F:\PythonStudy\day28\file1'
path2 = r'F:\PythonStudy\day28\file2'
print(jy(path1,path2))

