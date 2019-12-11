# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/12/10 9:41
# @Software       : Python_study
# @Python_verison : 3.7
'''
-- 29、查询每门课程被选修的学生数；
select score.score_course_id,count(1) from t_score score group by score.score_course_id;


-- 30、查询出只选修了一门课程的全部学生的学号和姓名；

select score.score_student_id,student.sname,COUNT(score.score_course_id) from t_score score
left join t_student student on score.score_student_id=student.s_id group by score.score_student_id HAVING COUNT(score.score_course_id)=1;



-- 31、查询男生、女生的人数；
select gender,count(gender) from t_student group by gender;

-- 32、查询姓“张”的学生名单；
select count(1) from t_student student where student.sname LIKE '张%';

-- 33、查询同名同姓学生名单，并统计同名人数；

select count(1)as count,student.sname from t_student student group by student.sname;


-- 34、查询每门课程的平均成绩，结果按平均成绩升序排列，平均成绩相同时，按课程号降序排列；

select avg(if(isnull(score.score_number),0,score.score_number))as 平均成绩 from t_score score group by score.score_course_id order by 平均成绩 asc,score.score_course_id desc;


-- 35、查询平均成绩大于85的所有学生的学号、姓名和平均成绩；

select student.s_id,student.sname,avg(if(ISNULL(score.score_number),0,score.score_number))as avg from t_score score left join t_student student on score.score_student_id=student.s_id group by score.score_student_id HAVING avg>85;

-- 36、查询课程名称为“数学”，且分数低于60的学生姓名和分数；
select student.sname,A.score_number from t_student student inner join
(select score.score_student_id,score.score_number from t_score score inner join t_course course on score.score_course_id=course.course_id where score.score_number<60 and course.course_name='生物')as A
on student.s_id=A.score_student_id;


-- 37、查询课程编号为003且课程成绩在80分以上的学生的学号和姓名；

select score.score_student_id,student.sname from t_score score left join t_student student on score.score_student_id=student.s_id where score.score_course_id=3 and score.score_number>80;

-- 38、求选了课程的学生人数

select count(distinct score_student_id) from t_score;

-- 39、查询选修“张磊”老师所授课程的学生中，成绩最高的学生姓名及其成绩；
select student.sname,B.score_number from t_student student left join
(select score.score_student_id,score.score_number from t_score score left join
(select course.c_teacher_id,course.course_id from t_teacher teacher left join t_course course on teacher.teacher_id=course.c_teacher_id where teacher.tname='张磊老师')as A
on score.score_course_id=A.course_id)as B
on student.s_id=B.score_student_id order by B.score_number DESC limit 1;


-- 40、查询各个课程及相应的选修人数；

select course.course_name,count(1) from t_score score left join t_course course on score.score_course_id=course.course_id group by course.course_id;

-- 41、查询不同课程但成绩相同的学生的学号、课程号、学生成绩；

select DISTINCT s1.score_course_id,s2.score_course_id,s1.score_number,s2.score_number from t_score as s1, t_score as s2 where s1.score_number = s2.score_number and s1.score_course_id != s2.score_course_id;

'''