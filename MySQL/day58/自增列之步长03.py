# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/11/27 14:53
# @Software       : Python_study
# @Python_verison : 3.7
'''
-- 自增列之步长：只能基于会话（登录）级别，一次登录后，设置步长，那么后面所有表的步长都是这个值，不像其他关系型数据库基于表

-- 1、会话级别（一次登录session）
	-- 查看会话步长
show session VARIABLES like'auto_incre%';			-- auto_increment_increment    value=1,表示默认步长就是1   auto_increment_offset：表示一个会话的初始值

	-- 设置会话步长
set session auto_increment_increment=2;

	-- 设置会话初始值
set session auto_increment_offset=10;

-- 2、全局级别（global）
	-- 查看全局步长
show global VARIABLES like'auto_incre%';			-- auto_increment_increment    value=1,表示默认步长就是1   auto_increment_offset：表示一个会话的初始值

	-- 设置会话步长
set global auto_increment_increment=2;

	-- 设置会话初始值
set global auto_increment_offset=10;
'''