# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/12/4 10:09
# @Software       : Python_study
# @Python_verison : 3.7
'''
-- 18、查询至少有一门课与学号为“001”的同学所学相同的同学的学号和姓名
select student.s_id,student.sname from t_student student inner join
(select score1.score_student_id from t_score score1 where score_student_id!=1 and score1.score_course_id in(select score.score_course_id from t_score score where score.score_student_id=1)
GROUP BY score_student_id)as A
ON student.s_id=A.score_student_id;


-- 19、查询至少学过学号为“001”同学所有课程的其他同学学号和姓名；
select student.s_id,student.sname from t_student student inner join
(select score1.score_student_id from t_score score1 where score_student_id!=1 and score1.score_course_id in(select score.score_course_id from t_score score where score.score_student_id=1)
GROUP BY score_student_id HAVING count(1)=(select count(score.score_course_id) from t_score score where score.score_student_id=1)) as A
ON student.s_id=A.score_student_id;-- 待补充学习

-- 20、查询和“002”号的同学学习的课程完全相同的其他同学学号和姓名；
select student.s_id,student.sname from t_student student inner join
(select score1.score_student_id from t_score score1 where score_student_id!=1 and score1.score_course_id in(select score.score_course_id from t_score score where score.score_student_id=1)
GROUP BY score_student_id HAVING count(1)=(select count(score.score_course_id) from t_score score where score.score_student_id=1)) as A
ON student.s_id=A.score_student_id;-- 待补充学习


'''