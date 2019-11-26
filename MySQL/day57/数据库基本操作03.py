# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/11/26 9:08
# @Software       : Python_study
# @Python_verison : 3.7
# 1、查看有哪些数据库
    # show databases;

# 2、使用或者进入数据库
    # use db1;

# 3、查看有哪些表
    # show tables;

# 4、创建数据库
    # create database db2;

# 5、删除数据库：
    # drop database db2;

# 6、创建用户(root)
    # 'jiangxi'@'127.0.0.1'表示该用户只能在ip：127.0.0.1下使用
    # create user jianghu;
    # create user 'jiangxi'@'127.0.0.1' identified by '123456;

# 7、删除用户
    # drop user jianghu;
    # drop user 'jianghu'@'127.0.0.1';

# 8、查看有哪些用户
    # select user from user;

# 9、权限管理
    # all privileages:  除grant外的所有权限
    # db1.* db1：       数据库的所有表的所有权限

    # 查看权限：show grants for yixiu@'127.0.0.1';
    # 分配权限：grant all privileages on db1.* to 'yixiu'@'127.0.0.1';
    # 删除select权限：revoke select on db1.user_info from 'yixiu'@'127.0.0.1'
                    # revoke all privileages on db1.* from 'yixiu'@'127.0.0.1'

# 10、忘记密码
# 启动免授权服务端
# mysqld --skip-grant-tables

# 客户端
# mysql -u root -p

# 修改用户名密码
# update mysql.user set authentication_string=password('666') where user='root';
# flush privileges;


