# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/11/28 9:16
# @Software       : Python_study
# @Python_verison : 3.7

'''
DROP TABLE
IF EXISTS t_department;

CREATE TABLE t_department (
	id INT auto_increment PRIMARY KEY,
	department_name VARCHAR (30) NOT NULL,
	department_id INT NOT NULL,
	UNIQUE (department_id)
) ENGINE=INNODB DEFAULT charset=utf8;

insert into t_department(department_name,department_id) VALUES('研发部',1),('运维部',2),('销售部',3),('后勤部',4),('市场部',5);



select * from t_department;
show create table t_department;

show SESSION VARIABLES like 'auto_inc%';



DROP TABLE
IF EXISTS t_user_info;

CREATE TABLE t_user_info (
	id INT auto_increment PRIMARY KEY,
	user_id INT NOT NULL,
	user_name VARCHAR (30) NOT NULL,
	user_department_id INT NULL,
	UNIQUE(user_id),
	CONSTRAINT fk_user_department FOREIGN KEY (user_department_id) REFERENCES t_department (department_id)
) ENGINE=INNODB DEFAULT charset=utf8;



INSERT INTO t_user_info (
	user_id,
	user_name
-- 	user_department_id
)
VALUES
-- 	(11, '小明', 1),
-- 	(12, '小可', 2),
-- 	(13, '的函', 1),
-- 	(14, 'kobe', 3),
-- 	(15, '小妹', 4),
-- 	(16, '科比', 3),
-- 	(9, 'king', 5),
	(111, 'dd');
select * from t_user_info;

SHOW CREATE TABLE t_user_info;

-- 1、内连接查询 where t1.id = t2.id
select * from t_department t1,t_user_info t2 where t1.department_id = t2.user_department_id;

-- 2、内连接查询 inner join

select * from t_department t1 INNER JOIN t_user_info t2 on t1.department_id=t2.user_department_id;

-- 3、外连接查询
-- 		左连接查询:表示左边的全部显示
select * from t_department t1 LEFT JOIN t_user_info t2 on t1.department_id=t2.user_department_id;

-- 		右连接查询:表示右边的全部显示
select * from t_department t1 RIGHT JOIN t_user_info t2 on t1.department_id=t2.user_department_id;






4、多个表连表查询
SELECT
	student.sname,course.course_name,score.score_number,class.caption
FROM
	t_score score
LEFT JOIN t_course course ON score.score_course_id = course.course_id

LEFT JOIN t_student student ON score.score_student_id = student.s_id

LEFT JOIN t_teacher teacher ON course.c_teacher_id = teacher.teacher_id

LEFT JOIN t_class class ON class.class_id = student.s_class_id;
'''
