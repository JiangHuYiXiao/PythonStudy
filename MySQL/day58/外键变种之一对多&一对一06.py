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
'''
