# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/11/27 10:27
# @Software       : Python_study
# @Python_verison : 3.7
'''

-- 1、主键补充：一个表只能有一个主键，但是一个主键可以由多列组成。

drop TABLE if EXISTS ats_info;
CREATE TABLE ats_info (
	id INT NOT NULL auto_increment,
	NAME VARCHAR (30) NOT NULL,
	department_id INT NOT NULL,
	PRIMARY KEY (id, department_id)
) ENGINE = INNODB DEFAULT CHARSET = utf8;

-- 2、外键补充：一个表可以有多个外键

show create table t_score;-- 查看表创建的语句以及下一个auto_increment的值


DROP TABLE
IF EXISTS t_score;

CREATE TABLE t_score (
	score_id INT (11) NOT NULL AUTO_INCREMENT,
	score_student_id INT (11) NOT NULL,
	score_course_id INT (11) NOT NULL,
	score_number INT (11) NOT NULL,
	PRIMARY KEY (score_id),
	KEY fk_score_student (score_student_id),
	KEY fk_score_course (score_course_id),
	CONSTRAINT fk_score_course FOREIGN KEY (score_course_id) REFERENCES t_course (course_id),
	CONSTRAINT fk_score_student FOREIGN KEY (score_student_id) REFERENCES t_student (s_id)
) ENGINE = INNODB AUTO_INCREMENT = 4 DEFAULT CHARSET = utf8;

-- 3、外键补充：一个表的外键可以由多个列组成，但是关联主表的这些列必须是联合主键

DROP TABLE
IF EXISTS t1_foreign_key;


CREATE TABLE t1_foreign_key (
	t1_id INT NOT NULL auto_increment,
	t1_pid INT NOT NULL,
	t1_name VARCHAR (20) NOT NULL,
	PRIMARY KEY (t1_id, t1_pid)
) ENGINE = INNODB DEFAULT charset = utf8;



DROP TABLE
IF EXISTS t2_foreign_key;

CREATE TABLE t2_foreign_key (
	t2_id INT auto_increment PRIMARY KEY,
	t2_pid INT NOT NULL,
	t2_name VARCHAR (20) NOT NULL,
	CONSTRAINT fk_t2_t1 FOREIGN KEY (t2_id, t2_pid) REFERENCES t1_foreign_key (t1_id, t1_pid)
) ENGINE = INNODB DEFAULT charset = utf8;

'''
