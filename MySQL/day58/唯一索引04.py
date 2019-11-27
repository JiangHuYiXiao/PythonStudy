# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/11/27 15:53
# @Software       : Python_study
# @Python_verison : 3.7
'''

-- 唯一索引：约束不能重复，但是可以为空，加速查找

DROP TABLE
IF EXISTS t_index1;

CREATE TABLE t_index1 (
	id INT auto_increment PRIMARY KEY,
	num INT NOT NULL,
	name1 VARCHAR (30) NOT NULL,
	UNIQUE uq1 (num) -- 唯一索引
) ENGINE = INNODB auto_increment = 10 DEFAULT charset = utf8;

insert into t_index1(num,name1) VALUES(1,'江西'),(2,'江湖');
insert into t_index1(num,name1) values(1,'jjj');				-- 因为设置了num为唯一索引，所以再次插入重复的num就会报错，[Err] 1062 - Duplicate entry '1' for key 'uq1'
select * from t_index1;


DROP TABLE
IF EXISTS t_index2;

CREATE TABLE t_index2 (
	id INT auto_increment PRIMARY KEY,
	num INT NOT NULL,
	name1 VARCHAR (30) NOT NULL,
	UNIQUE uq1 (name1,num) -- 联合唯一索引，表示name1和num不能完全重复
) ENGINE = INNODB auto_increment = 10 DEFAULT charset = utf8;

insert into t_index2(num,name1) VALUES(1,'江西'),(2,'江湖');
insert into t_index2(num,name1) VALUES(1,'江哥'),(2,'江姐');
insert into t_index2(num,name1) VALUES(1,'江哥'),(3,'江姐');		-- [Err] 1062 - Duplicate entry '江哥-1' for key 'uq1'

select * from t_index2;

'''