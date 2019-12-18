# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/12/18 15:54
# @Software       : Python_study
# @Python_verison : 3.7
'''
-- 10、索引不是越多越好因为需要创建索引文件，数据结构，索引一般建议索引建立2-3个


show index from big_table;
drop index tname_index1 on big_table;
create unique index tname_index on big_table(tname);


-- 11、索引无法命中的情况
-- 	like
select * from big_table where tname like'%湖%';


-- 2、or 当or条件中有未建立索引的列才失效
select * from big_table where tname='江湖111' or gender ='男';


-- 3、使用函数
select * from big_table where REVERSE(tname)='江湖111';


-- 4、类型不一致
select * from big_table where tname=4444;

-- 5、!=,但是如果列是主键则还是会走索引
select * from big_table where tname!=4444;

-- 6、>,但是如果列是主键则还是会走索引

select * from big_table where tname>4444;


-- 7、order by，如果所排序的列没有索引，则无法走索引，如果排序的列是索引则会走索引，如果是主键则还是会走索引
select * from big_table order by tname desc;
select * from big_table order by id desc;

-- 8、联合索引 没哟遵循最左前缀
show index from big_table;
create index tname_gender_index on big_table(tname,gender);
select * from big_table where tname='江湖4444' and gender='男';  -- 命中索引
select * from big_table where gender='男'; -- 无法命中索引
'''