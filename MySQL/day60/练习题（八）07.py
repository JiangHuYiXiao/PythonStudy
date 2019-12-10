# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/12/9 8:55
# @Software       : Python_study
# @Python_verison : 3.7
'''
-- 26、课程平均分从高到低显示（现实任课老师）；
select avg(score.score_number),score.score_course_id,teacher.tname from t_score score left join t_course course on score.score_course_id=course.course_id
left join t_teacher teacher on course.c_teacher_id= teacher.teacher_id group by score.score_course_id;

-- if(ISNULL(score_number),0,score_number)  相当于我们的三目运算符     条件成立的结果 if 条件 else 条件不成立的结果
select avg(if(ISNULL(score_number),0,score_number)),score.score_course_id,teacher.tname from t_score score left join t_course course on score.score_course_id=course.course_id
left join t_teacher teacher on course.c_teacher_id= teacher.teacher_id group by score.score_course_id;

-- 27、查询各科成绩前三名的记录:(不考虑成绩并列情况)

select* FROM
(select
score_student_id,
score_course_id,
score_number,
(select score.score_number from t_score score where score.score_course_id=A.score_course_id group by score.score_number order by score.score_number desc limit 0,1)as 第一名,
(select score.score_number from t_score score where score.score_course_id=A.score_course_id group by score.score_number order by score.score_number desc limit 2,1)as 第三名
from t_score as A)as C WHERE C.score_number> C.第三名 and C.score_number<C.第一名 group BY C.score_course_id;


-- 28、查询每门课程成绩最好的前两名；

select* FROM
(select
score_student_id,
score_course_id,
score_number,
(select score.score_number from t_score score where score.score_course_id=A.score_course_id group by score.score_number order by score.score_number desc limit 0,1)as 第一名,
(select score.score_number from t_score score where score.score_course_id=A.score_course_id group by score.score_number order by score.score_number desc limit 2,1)as 第三名
from t_score as A)as C WHERE C.score_number> C.第三名 and C.score_number<C.第一名 group BY C.score_course_id;
'''