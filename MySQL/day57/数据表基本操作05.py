# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/11/26 11:11
# @Software       : Python_study
# @Python_verison : 3.7

# 1、创建数据表
# create table addrs_info(id int not null,name varchar(32) null) engine = innobd default charset=utf8;
    # 创建数据表的定长的列建议放前面
    # not null 不能为空
    # null 可以为空
    # engine = innobd       是mysql的一个存储引擎，支持事务处理等高级处理，支持外键
    # charset=utf8          编码方式，解决编码问题

# create table addrs(id int auto_increment primary key,name varchar(20) null,age char(4) not null) engine=innodb default charset=utf8;
    # auto_increment 自增长，必须和primary key一起使用
    # primary key    主键，约束每一行记录的唯一标识，加速查找
# create table addrs(id int signed auto_increment primary key,name varchar(20) null,age char(4) not null) engine=innodb default charset=utf8;
    # signed表示有符号，就是支持正数负数。

# 2、查询表：
# show tables;            # 查询有哪些表
# desc addrs;             # 查询表结构

# 3、往数据表中插入数据
# insert into addrs(id,name,age) values(1,'woqu',18);
# insert into addrs(name,age) values('woqu',18);                # 因为设置了自增长，所以可以这么设置，自增的那一列不插入


# 4、删除数据表
# delete from addrs;          # 删除表数据
# truncate table addrs;         # 删除表数据
# drop table addrs;           # 表都删除


# 5、给数据表添加外键，外键是为了保持数据一致性，完整性和节省空间----***使用场景，下拉选择值***
# 一个表的外键必须是另一个表的唯一索引，主键约束和唯一性约束都是唯一性索引。
# create table ats_info(
#     aid int auto_increment primary key,
#     name varchar(40)not null,
#     sex char(2) null,
#     constraint fk_ats_pp foreign key ('aid',) references person_info('pid')          # 创建约束
# ) engine=innodb default charset=utf8;

# create table person_info(pid int auto_increment primary key,name varchar(40)not null) engine=innodb default charset=utf8;


# 6、修改数据表
# 增加列：alter table 表名 add 列名 类型
# 删除列：alter table 表名 drop column 列名
# 修改列：
#         alter table 表名 modify column 列名 类型;  -- 类型
#         alter table 表名 change 原列名 新列名 类型; -- 列名，类型
# 添加主键：
#         alter table 表名 add primary key(列名);
# 删除主键：
#         alter table 表名 drop primary key;
#         alter table 表名  modify  列名 int, drop primary key;
# 添加外键：alter table 从表 add constraint 外键名称（形如：FK_从表_主表） foreign key 从表(外键字段) references 主表(主键字段);
# 删除外键：alter table 表名 drop foreign key 外键名称
# 修改默认值：ALTER TABLE testalter_tbl ALTER i SET DEFAULT 1000;
# 删除默认值：ALTER TABLE testalter_tbl ALTER i DROP DEFAULT;

# 7、删除表数据
# delete from addrs where id =2;

# 8、更新表数据
# update addrs set age=199;

# 9、查询表数据
# select * from addrs;