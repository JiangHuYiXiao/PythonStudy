# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/11/27 11:03
# @Software       : Python_study
# @Python_verison : 3.7
'''
drop table if exists t1;
create table t1(
t1_id int auto_increment primary key,
t1_age int not null
)engine=INNODB auto_increment=10 default charset=utf8;

-- 1、查看创建表的结构
desc t1;

insert into t1(tq_id,t1_age) VALUES(22,12);

insert into t1(t1_id,t1_age) VALUES(1,12),(2,1221);
-- 2、查看下一个auto_increment的值

show create table t1;

insert into t1(t1_age) VALUES(3),(5);

-- 3、查看下一个auto_increment的值
show create table t1;

select * from t1;

-- 4、修改auto_increment默认值
ALTER TABLE t1 auto_increment=20;

'''