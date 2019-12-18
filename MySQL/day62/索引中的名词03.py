# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/12/18 15:52
# @Software       : Python_study
# @Python_verison : 3.7
'''
-- 8、索引中的名词
-- 覆盖索引：
select * from big_table where id=999;   -- 0.0.17s  利用索引查询


select id from big_table where id=999;   -- 0.002s  利用索引查询索引列，这种就是覆盖索引


-- 索引合并：把多个单列索引一起使用就是索引合并
select * from big_table where id =999 and tname='江湖999';


-- 9、最左前缀匹配:（针对联合索引）
-- 		意思就是通过这个id，tname联合索引，只能先id查询
-- 		联合索引查询效率>索引合并查询效率
select * from big_table where id=111;			-- 这样会命中索引，走索引
select * from big_table where id=111 and tname='江湖111';			-- 这样会命中索引，走索引
select * from big_table where tname='江湖111' and id=111;			-- 这样不会命中索引，不走索引
select * from big_table where tname='江湖111';			-- 这样不会命中索引，不走索引
'''