# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/10/30 9:39
# @Software       : server
# @Python_verison : 3.7
import os
import pickle
from core.user import User
from conf import setting
def login(msg):
    print(msg)


def register(msg):
# 存储username，password到userinfo文件中,并且记录username
# 创建他的家目录
# 记录用户的初始磁盘配额
# 记录文件大小
# 记录用户当前所在的目录
    user_obj = User(msg['username'])             # 记录username
    pickle_path = os.path.join(setting.pickle_path,msg['username'])
    with open(pickle_path,'wb') as f:
        pickle.dump(user_obj,f)
    os.mkdir(user_obj.home)             # 创建他的家目录
    with open(setting.user_info,'a') as f:
        f.write('%s|%s|%s'%(msg['username'],msg['password'],pickle_path))
    return True
def upload(msg):
    print(msg)

def download(msg):
    print(msg)