# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/12/18 15:52
# @Software       : Python_study
# @Python_verison : 3.7
'''
-- 5、查看表中索引有哪些
show index from big_table;

-- 6、索引类型分为hash索引，btree索引
-- hash索引：索引文件为id，hash值，内存地址，在查询单个值的时候效率较高，在查询范围的时候效率较低。
-- btree索引：是一个二叉树模型，左边的值比它的父节点的值小，右边的值比父节点大，查找一个数，最多查2**n次，我们在实际工作用的基本是btree索引，
-- 索引的类型，和我们表的存储引擎也有关系的，一般innodb用的是btree索引



-- 7、索引的创建: 索引创建会创建索引文件，加速查找，或者约束，但是新增、修改、删除会变慢，因为不仅需要更新表，还要更新索引文件。

		-- 7.1主键索引：
-- 				1、在创建表的时候创建主键索引
drop table if EXISTS big_table;
create table big_table(
id int auto_increment PRIMARY KEY ,
tname VARCHAR(30) not null,
email VARCHAR(40) not null,
gender varchar(4) not null)ENGINE=INNODB charset=utf8;

-- 				2、在创建表后面添加主键索引
alter table big_table add PRIMARY key(id);

-- 				3、删除主键索引
alter table big_table drop primary key;


-- 7.2 唯一索引
-- 				1、在创建表的时候创建
drop table if EXISTS big_table;
create table big_table(
id int auto_increment PRIMARY KEY ,
tname VARCHAR(30) not null,
email VARCHAR(40) not null,
gender varchar(4) not null,
UNIQUE tname_index (tname))ENGINE=INNODB charset=utf8;

-- 				2、在后面添加唯一主键
create UNIQUE INDEX tname_index on big_table(tname);

-- 				3、在删除唯一主键
alter table big_table drop index tname_index;

show index from big_table;


-- 7.3普通索引
-- 				1、在创建表的时候创建
drop table if EXISTS big_table;
create table big_table(
id int auto_increment PRIMARY KEY ,
tname VARCHAR(30) not null,
email VARCHAR(40) not null,
gender varchar(4) not null,
index tname_index (tname))ENGINE=INNODB charset=utf8;

-- 				2、后面添加
create index tname_index on big_table(tname);

show index from big_table;

-- 				3、删除普通索引
alter table big_table drop index tname_index;

drop index tname_index on big_table;


-- 7.4联合索引（联合普通索引，联合主键索引，联合唯一索引）
-- 				1、在创建表的时候创建
-- 联合主键索引
drop table if EXISTS big_table;
create table big_table(
id int auto_increment,
tname VARCHAR(30) not null,
email VARCHAR(40) not null,
gender varchar(4) not null,
PRIMARY KEY(id,tname))ENGINE=INNODB charset=utf8;

-- 联合唯一索引
drop table if EXISTS big_table;
create table big_table(
id int auto_increment,
tname VARCHAR(30) not null,
email VARCHAR(40) not null,
gender varchar(4) not null,
unique id_tname_index(id,tname))ENGINE=INNODB charset=utf8;

-- 联合普通索引
drop table if EXISTS big_table;
create table big_table(
id int auto_increment,
tname VARCHAR(30) not null,
email VARCHAR(40) not null,
gender varchar(4) not null,
index id_tname_index(id,tname))ENGINE=INNODB charset=utf8;

-- 				2、后面添加
alter table big_table add PRIMARY key(id,tname);

create UNIQUE INDEX tname_index on big_table(id,tname);

create index tname_index1 on big_table(id,tname);


-- 最左前缀匹配:
-- 		意思就是通过这个id，tname联合索引，只能
select * from big_table where id=111;			-- 这样会命中索引，走索引
select * from big_table where id=111 and tname='江湖111';			-- 这样会命中索引，走索引
select * from big_table where tname='江湖111' and id=111;			-- 这样不会命中索引，不走索引
select * from big_table where tname='江湖111';			-- 这样不会命中索引，不走索引

drop index tname_index on big_table;
show index from big_table;

-- 				3、删除索引
alter table big_table drop index tname_index;
'''