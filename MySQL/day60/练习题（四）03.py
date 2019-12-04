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

-- 14、查询学过“李平”老师所教的所有课的同学的学号、姓名；
select student.s_id,student.sname from t_student student where student.s_id in(
select score.score_student_id from t_score score where score.score_course_id in(
select course.course_id from t_course course left join t_teacher teacher on course.c_teacher_id=teacher.teacher_id where teacher.tname='李平老师'));

-- 15、查询课程编号“002”的成绩比课程编号“001”课程低的所有同学的学号、姓名；
select student.s_id,student.sname from t_student student INNER JOIN
(select A.score_student_id from
(select score.score_number,score.score_student_id from t_score score where score.score_course_id=1)as A
left join
(select score.score_number,score.score_student_id from t_score score where score.score_course_id=2)as B
on A.score_student_id=B.score_student_id where A.score_number>B.score_number)as C
ON student.s_id=C.score_student_id;


-- 16、查询有课程成绩小于60分的同学的学号、姓名；
select student.s_id,student.sname from t_student student inner join t_score score on student.s_id=score.score_student_id where score.score_number<60 GROUP BY score.score_student_id; -- 使用group by去重



select DISTINCT student.s_id,student.sname from t_student student inner join t_score score on student.s_id=score.score_student_id where score.score_number<60; -- 使用distinct去重，效率低



-- 17、查询没有学全所有课的同学的学号、姓名
select student.s_id,student.sname from t_student student
inner join
t_score score on student.s_id=score.score_student_id group by score.score_student_id HAVING COUNT(1)<(select count(1) from t_course);

select * from t_score;

'''