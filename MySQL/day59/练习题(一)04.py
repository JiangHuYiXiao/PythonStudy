# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/11/29 13:52
# @Software       : Python_study
# @Python_verison : 3.7
'''
-- 1、查询成绩表大于60分的数据
select * from t_score where score_number>60;

-- 2、查询课程表中每个老师任课数。
select  t.c_teacher_id,count(*) from t_course t group BY t.c_teacher_id;

-- 3、查询课程表中teacher_id对应的中文名称。
select c_teacher_id,tname from t_course t1 left join t_teacher t2 on t1.c_teacher_id=t2.teacher_id;

-- 4、查询学生表中class_id对应的班级名称。
select t1.s_class_id,t2.caption from t_student t1 left join t_class t2 on t1.s_class_id=t2.class_id;

-- 5、查询学生表中男生数和女生数。
select gender,count(gender) FROM t_student GROUP BY gender;
'''
