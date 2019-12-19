# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/12/19 14:49
# @Software       : Python_study
# @Python_verison : 3.7
'''
-- 14、慢日志记录

	-- 查询全局变量，包含query的
show variables like '%query%';
-- 		slow_query_log = OFF                            是否开启慢日志记录
-- 		long_query_time = 2                              时间限制，超过此时间，则记录
-- 		slow_query_log_file = /usr/slow.log        日志文件
-- 		log_queries_not_using_indexes = OFF     未使用索引的搜索是否记录

set global slow_query_log=ON;
commit;
set global slow_query_log_file='D:\mysql_log';
set global long_query_time=1;
'''