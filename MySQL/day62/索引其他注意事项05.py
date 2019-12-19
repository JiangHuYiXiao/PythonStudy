# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/12/19 8:48
# @Software       : Python_study
# @Python_verison : 3.7
'''
-- 12、索引注意事项
1、避免使用select *,需要哪几列值就查询哪几列
2、尽量使用count(1),，避免使用count(*)
3、列中的值重复较少的不适合建立索引，比如：性别
4、建立索引，尽量使用短索引
create index id_index on big_table(tname(16));  表示tname字段前16个字段建立索引，尤其是针对哪种text类型
5、联合索引查询效率大于索引合并（前提是查询时候需要使用多个条件）
6、创建表时如果不是定长，尽量使用char
7、固定长度的字段优先变长的字段
8、使用join代替子查询
9、连表查询时字段类型要保持一致
'''