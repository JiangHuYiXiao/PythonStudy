# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/12/2 8:43
# @Software       : Python_study
# @Python_verison : 3.7
'''

-- 6、临时表
select * from t_score where score_number>60;-- 把他查询的结果可以作为一个临时表

select score_id,score_number from (select * from t_score where score_number>60) as B WHERE score_number=100;

select score_id from (select * from t_score where score_number>60);			-- 必须写as B
select s_id from (select * from t_score where score_number>60)as b;			-- 必须查询的列必须是临时表中存在的列

'''