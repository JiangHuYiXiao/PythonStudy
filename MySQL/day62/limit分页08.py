# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/12/20 8:49
# @Software       : Python_study
# @Python_verison : 3.7
'''
-- 15、limit分页查询


-- 第一页
select * from big_table limit 10;

-- 第二页
select * from big_table limit 10,10;


show index from big_table;

-- 方案1：用户只能每次看一页，后面的不让看

-- 优化方案2：
select * from big_table where id in(select id from big_table limit 10,10);

-- 优化方案3：记录当前页的最大、最小id，可以切换到上一页，下一页
-- 上一页
select * from big_table where id<min_id order by id desc limit 10;

-- 后一页
select * from big_table where id>max_id limit 10;

-- 上一页 186,187,[192],193,194,195,196 下一页 当前页为192
-- 优化方案4：可以切换到上一页，下一页，以及跳转到附近的其他页
select * from big_table where id in(select id from(select id from big_table where id >max_id limit 40)as A order by A.id desc limit 10);


'''