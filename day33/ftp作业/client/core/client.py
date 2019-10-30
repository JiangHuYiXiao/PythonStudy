# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/10/29 9:01
# @Software       : client
# @Python_verison : 3.7
'''

'''
from core.auth_client import Auth
def main():
    # 选择为何种操作-菜单
    auth_obj = None
    start_list = [('注册','register'),('登录','login'),('退出','quit')]      # 这样做是为了在元组中以后可以添加方法、类等，以后可以用反射来使用他们的属性
    for index,item in enumerate(start_list,1):              # index从1开始
        print(index,item[0])
    while True:
        try:
            num = int(input('>>>'))
            func_str = start_list[num-1][1]         # 得到字符串数据类型的方法
            print(func_str)
        except:
            print('你输入的信息有误')

        if hasattr(Auth,func_str):          # 登录、注册
            auth_obj = Auth()
            func = getattr(auth_obj,func_str)
            ret = func()
            if ret:
                break
        elif auth_obj:
            auth_obj.sk.close()
            break
        else:
            break
