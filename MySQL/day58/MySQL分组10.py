# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/11/28 19:25
# @Software       : Python_study
# @Python_verison : 3.7
'''
		-- 分组 gruoup by 必须在where之后，order by之前
		-- 对聚合函数的结果二次筛选必须用having条件，不能用where
select count(*),user_department_id from t_user_info group BY user_department_id;

select count(*),user_department_id from t_user_info where user_department_id=3 group BY user_department_id;

select count(*),user_id,user_department_id from t_user_info group BY user_department_id having user_id >11 ORDER BY user_id desc;
'''