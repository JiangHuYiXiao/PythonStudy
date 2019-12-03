# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/12/3 9:38
# @Software       : Python_study
# @Python_verison : 3.7
'''
-- 13、查询学过“001”并且也学过编号“002”课程的同学的学号、姓名
select A.score_student_id,student.sname from t_student student INNER join
(select score.score_student_id from t_score score left join t_course course on score.score_course_id=course.course_id
where course.course_id=1 or course.course_id=2 GROUP by score_student_id HAVING count(score_student_id)>1)as A on student.s_id=A.score_student_id;

-- 14、查询学过“叶平”老师所教的所有课的同学的学号、姓名

select course.course_id from t_course course left join t_teacher teacher on course.c_teacher_id=teacher.teacher_id where teacher.tname='李平老师';
'''