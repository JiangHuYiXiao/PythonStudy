# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/12/2 8:50
# @Software       : Python_study
# @Python_verison : 3.7
'''
-- 7、查询平均成绩大于60分的同学的学号和平均成绩；
select score.score_student_id,avg(score.score_number) from t_score score group by score.score_student_id HAVING avg(score.score_number)>60;

-- 8、查询平均成绩大于60分的同学的学号和平均成绩以及学生姓名；
select b.avg(score.score_number) from
(select score.score_student_id,avg(score.score_number) from t_score score group by score.score_student_id HAVING avg(score.score_number)>60) as b
left JOIN
t_student student on b.score_student_id=student.s_id;   -- 报错，因为会误认为avg是一个函数，而不是一个结果，所以我们应该把avg的结果作为一列,所以以后有聚合函数的时候查询出来的结果需要as为一个新列


select b.score_student_id,student.sname,b.avg_number from
(select score.score_student_id,avg(score.score_number) as avg_number from t_score score group by score.score_student_id HAVING avg(score.score_number)>60) as b
left JOIN
t_student student on b.score_student_id=student.s_id;


-- 9、查询所有同学的学号、姓名、选课数、总成绩

select student.s_id,student.sname,b.count,b.score_student_id,b.sum from t_student student
left join
(select count(score.score_student_id)as count,score.score_student_id,sum(score.score_number) as sum from t_score score GROUP BY score.score_student_id) as b
on student.s_id=b.score_student_id;


select student.s_id,student.sname,count(score.score_student_id),score.score_student_id,sum(score.score_number) from t_student student
left join t_score score on student.s_id=score.score_student_id GROUP BY score.score_student_id order by student.s_id asc;


-- 10、查询姓李老师的个数
select count(1) from t_teacher where tname like'李%';

-- 11、查询没有学过李平老师课的同学的学号和姓名

select student.s_id,student.sname from t_student student where student.s_id not in(
select score.score_student_id from t_score score where score.score_course_id in (
select course.course_id from t_teacher teacher left join t_course course on teacher.teacher_id=course.c_teacher_id where teacher.tname='李平老师') group by score.score_student_id);

-- 12、查询“生物”课程比“物理”课程成绩高的所有学生的学号

select * from
(select score.score_student_id,score.score_number from t_score score left join t_course course on score.score_course_id=course.course_id where course.course_name='生物')as A
INNER JOIN
(select score.score_student_id,score.score_number from t_score score left join t_course course on score.score_course_id=course.course_id where course.course_name='物理')as B
ON A.score_student_id=B.score_student_id where A.score_number>B.score_number;

;
'''