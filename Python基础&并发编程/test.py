# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/11/6 9:14
# @Software       : Python_study
# @Python_verison : 3.7

# import pytest
# # 不带参数时默认 scope="function"
# @pytest.fixture()               # function，运行两次
# def login():
#     print("输入账号，密码先登录")
# def test_s1(login):
#     print("用例 1：需要登录操作")
# def test_s2(login):         # 调用login，然后执行login（）
#     print("用例 2：登录之后其它动作")
#
#
#
#
# import pytest
# @pytest.fixture(scope="module")                 # 只运行一次
# def open():
#     print("打开浏览器，并且打开百度首页")
#
# def test_s3(open):
#     print("用例 1：搜索 python-1")
#
# def test_s4(open):
#     print("用例 2：搜索 python-2")
#
# if __name__ == "__main__":
#     pytest.main()



class TestClass:
    def __init__(self):
        self.name = 'testcase'
    def __str__(self):
        return self.realname
t = TestClass()
print(t)
