# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/12/12 17:04
# @Software       : Python_study
# @Python_verison : 3.7
'''
-- 3、视图的创建，本质就是一个临时表，虚拟的，这个临时表是动态查询的
create view v1 as select * from t_score score where score.score_number>80;

-- 往视图中 插入数据就是我们的insert into 不能直接往视图中添加
insert into t_score(score_student_id,score_course_id,score_number) VALUES(13,1,100);

-- 4、查询视图
select * from v1;			-- 插入的数据已经更新到视图中


-- 5、删除视图
drop view v1;

-- 6、修改视图
alter view v1 as select * from t_score score where score.score_number>90;

'''