# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/12/10 9:41
# @Software       : Python_study
# @Python_verison : 3.7
'''
-- 29、查询每门课程被选修的学生数；
select score.score_course_id,count(1) from t_score score group by score.score_course_id;
'''