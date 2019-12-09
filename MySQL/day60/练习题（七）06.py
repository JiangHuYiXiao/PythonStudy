# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/12/6 9:08
# @Software       : Python_study
# @Python_verison : 3.7
'''
-- 24、查询各科成绩最高和最低的分：以如下形式显示：课程ID，最高分，最低分；

select score_course_id,max(score_number),min(score_number) from t_score score group by score.score_course_id;


-- 25、按各科平均成绩从低到高和及格率的百分数从高到低顺序；
-- case when 条件1 then 结果1 else 结果2 end
select score.score_course_id,avg(score.score_number) as 平均成绩,
sum(case when score.score_number<60 then 0 else 1 end),sum(1),sum(case when score.score_number<60 then 0 else 1 end)/sum(1) jgl
from t_score score group by score.score_course_id order by 平均成绩 asc,jgl desc;

'''