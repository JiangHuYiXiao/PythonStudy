# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/11/28 19:34
# @Software       : Python_study
# @Python_verison : 3.7
'''
-- 外键变种一对多
	-- 示例：一个部门下有多个员工，也就是一个部门t1_department_id对应多个t1_user_name
DROP TABLE
IF EXISTS t1_department;

CREATE TABLE t1_department (
	id INT auto_increment PRIMARY KEY,
	t1_department_name VARCHAR (30) NOT NULL,
	t1_department_id INT NOT NULL,
	UNIQUE (t1_department_id)

) ENGINE = INNODB DEFAULT charset = utf8;

DROP TABLE
IF EXISTS t1_user_info;

CREATE TABLE t1_user_info (
	id INT auto_increment PRIMARY KEY,
	t1_user_name VARCHAR (20) NOT NULL,
	t1_user_department_id INT NOT NULL,
	CONSTRAINT fk_t1_user_department FOREIGN KEY (t1_user_department_id) REFERENCES t1_department (t1_department_id)
) ENGINE = INNODB DEFAULT charset = utf8;

INSERT INTO t1_department (
	t1_department_name,
	t1_department_id
)
VALUES
	('研发部', 11),('考勤部', 12),('假期部', 13);


INSERT INTO t1_user_info (
	t1_user_name,
	t1_user_department_id
)
VALUES
	('huhu', 11),
	('jiangjiang', 12),
	('kao', 13),
	('zhu', 13),
	('niu', 13);

select * from t1_department;
select * from t1_user_info;



-- 外键变种之一对一：
-- 		博客园的用户表和博客地址表,一个用户只有一个博客地址，注册了博客后就不能再注册了，


DROP TABLE
IF EXISTS t_blog_user;



CREATE TABLE t_blog_user (
	id INT auto_increment PRIMARY KEY,
	user_name VARCHAR (30) NOT NULL,
	user_id INT NOT null,
	UNIQUE uq1(user_id)
) ENGINE = INNODB DEFAULT charset = utf8;

insert into t_blog_user(user_name,user_id) values('jiangtao_jiang',110),('tao_jiang',111),('jiangtao',112),('jianghu',115),('taotao',113),('taobao',114);		-- 唯一索引不允许重复
insert into t_blog_user(id,user_name,user_id) values(1,'zibaoba',11),(2,'人生',365);			-- 主键不允许重复
insert into t_blog_user(user_name,user_id) values('jiangtao_jiansfg',110);
select * from t_blog_user;


DROP TABLE
IF EXISTS t_cnblogs;

CREATE TABLE t_cnblogs (
	id INT auto_increment PRIMARY KEY,
	blog_addr VARCHAR (40) NOT NULL,
	cnblogs_user_id INT NOT NULL,
	UNIQUE (blog_addr),								-- 唯一索引，表示单独不允许重复
	UNIQUE (cnblogs_user_id),					-- 唯一索引，表示单独不允许重复
-- 	UNIQUE uq2 (blog_addr, cnblogs_user_id),	-- 表示两个字段不能完全一样

	CONSTRAINT fk_user_cnblogs FOREIGN KEY (cnblogs_user_id) REFERENCES t_blog_user (user_id)
) ENGINE = INNODB DEFAULT charset = utf8;

insert into t_cnblogs(blog_addr,cnblogs_user_id) values('yixifsdfu',111),('sdf',112);
select * from t_cnblogs;
'''
