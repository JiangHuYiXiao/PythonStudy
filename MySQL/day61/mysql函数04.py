# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/12/12 19:46
# @Software       : Python_study
# @Python_verison : 3.7
'''
-- 1、内置函数
select CURDATE();     -- 日期时间
select sum(55+32+3223);
select char_LENGTH('dfdsdfsfs');   -- 长度
select CONCAT('wer','wegfr','werewr23432');  -- 拼接

-- 格式化时间
select CURRENT_TIMESTAMP();			-- 时间 年月日时分秒


DROP TABLE
IF EXISTS t_bolg_time;

CREATE TABLE t_bolg_time (
	id INT auto_increment PRIMARY KEY,
	user_name VARCHAR (20) NOT NULL,
	ctime DATETIME
) ENGINE = INNODB DEFAULT charset = utf8;

insert into t_bolg_time(user_name,ctime) values('jianghu','2019-11-10 11:02:02'),('jiangxi','2019-11-11 11:02:02'),('jiang','2019-11-10 11:02:02'),('xixi','2019-11-10 11:02:02');
drop table t_bolg_time;
select * from t_bolg_time;

select DATE_FORMAT(ctime,'%Y-%m'),count(1)from t_bolg_time group by DATE_FORMAT(ctime,'%Y-%m');   -- 对时间进行分组


-- 2、自定义函数
-- 创建
delimiter //
create FUNCTION fun1(arg1 int,arg2 int)
returns int
BEGIN
 declare num int;
 set num=arg1+arg2;
 return(num);
END //
delimiter;

-- 调用函数
select fun1(1,2);

-- 删除函数
drop function fun1;

-- 函数必须有返回值，函数里面不能写select语句
'''