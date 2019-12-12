# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/12/12 16:54
# @Software       : Python_study
# @Python_verison : 3.7
'''
-- 1、union 上下表连接，连接的两个表查询的列数必须一致，且如果数据重复会自动去重

select s_id,sname from t_student
union
select teacher_id,tname from t_teacher;

select s_id,sname from t_student
union
select s_id,sname from t_student;



-- 2、unionall 上下表连接，不自动去重
select s_id,sname from t_student
union all
select s_id,sname from t_student;
'''