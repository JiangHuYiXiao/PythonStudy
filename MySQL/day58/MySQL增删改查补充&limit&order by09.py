# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/11/28 17:19
# @Software       : Python_study
# @Python_verison : 3.7
'''
-- 1、增加
    -- 单个插入
INSERT INTO t_department(department_name,department_id) VALUES('测试部',60);
    -- 多个插入
INSERT INTO t_department(department_name,department_id) VALUES('测试部',7),('需求部',8);
    -- 来源与其他表
INSERT INTO t_department(department_name,department_id) select name,id from user_info;
INSERT INTO t_department(department_name,department_id) select name,(select id from user) from user_info;

select * from t_department;

-- 2、删除

delete from t1;-- 删除后自增列值不会重新取值
drop table t1;
TRUNCATE table t1;-- 删除后自增列值会重新取值

-- 3、改

CREATE TABLE t1 (
	id INT auto_increment PRIMARY KEY,
	NAME VARCHAR (10) NOT NULL
) ENGINE = INNODB DEFAULT charset = utf8;
insert into t1(name) values('jianghu');
select * from t1;
update t1 set t1.NAME='jianghuyixiao' where id=1;

-- 4、查找 其他方法
    -- 条件
select * from t_user_info;

select * from t_user_info where user_department_id is NULL;

select * from t_user_info t1 where t1.user_department_id is NULL;

select * from t_user_info where t_user_info.id IN(1,2,3);

select * from t_user_info where t_user_info.id not IN(1,2,3);

select * from t_user_info where t_user_info.id between 1 and 3;

select * from t_user_info where t_user_info.id between 1 and 3;

select * from t_user_info t1 where id in(select teacher_id from t_teacher);
SELECT
    student_id,
    (select num from score as s2 where s2.student_id=s1.student_id and course_id = 1) as 语文,
    (select num from score as s2 where s2.student_id=s1.student_id and course_id = 2) as 数学,
    (select num from score as s2 where s2.student_id=s1.student_id and course_id = 3) as 英语
from score as s1;

    -- 通配符

select * from t_user_info t1 where user_name like '小%';			-- 多个字符

select * from t_user_info t1 where user_name like '小_';		-- 一个字符


    -- 限制
select * from t_user_info limit 5;		-- 查询前五行

select * from t_user_info limit 0,1;		-- 从0开始查询，查一行数据

select * from t_user_info limit 2,5;		-- 从第三行开始查询，查5行数据


    -- 排序
select * from t_user_info order by user_id desc;   -- 从大到小排序

select * from t_user_info order by user_id asc;   -- 从小到大排序
'''