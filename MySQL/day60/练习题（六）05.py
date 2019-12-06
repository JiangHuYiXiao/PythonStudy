# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/12/6 8:24
# @Software       : Python_study
# @Python_verison : 3.7
'''
-- 21、删除学习“李平”老师课的score表记录
DELETE from t_score score where score.score_course_id in(
select course.course_id from t_teacher teacher inner join t_course course on teacher.teacher_id=course.c_teacher_id where teacher.tname='李平老师');


-- 22、向SC表中插入一些记录，这些记录要求符合以下条件：①没有上过编号“002”课程的同学学号；②插入“002”号课程的平均成绩；
insert into t_score(score_student_id,score_course_id,score_number)
select score_student_id,4,(select avg(score_number) from t_score where score_course_id=2) from t_score score where score.score_course_id!=2 group by score_student_id;


-- 23、按平均成绩从低到高 显示所有学生的“生物”、“物理”、“体育”三门的课程成绩，按如下形式显示： 学生ID,生物,物理,体育,有效课程数,有效平均分

select score_student_id,
(select score_number from t_score as sw where score_course_id in(select course_id from t_course where course_name='生物') and sw.score_student_id= sc.score_student_id )as 生物成绩,
(select score_number from t_score as wl where score_course_id in(select course_id from t_course where course_name='物理') and wl.score_student_id= sc.score_student_id) as 物理成绩,
(select score_number from t_score as ty where score_course_id in(select course_id from t_course where course_name='体育') and ty.score_student_id= sc.score_student_id) as 体育成绩,
count(sc.score_course_id) as 有效课程数,
avg(sc.score_number) as 平均成绩
from t_score as sc group by sc.score_student_id order by 平均成绩;
'''