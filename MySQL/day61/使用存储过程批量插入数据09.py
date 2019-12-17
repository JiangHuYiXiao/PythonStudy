# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/12/17 13:55
# @Software       : Python_study
# @Python_verison : 3.7
'''
delimiter//
drop PROCEDURE if exists insert_t;
create PROCEDURE insert_t()
BEGIN
	declare auto_num int DEFAULT 1;
	drop table if exists big_table;
	create table big_table(
	id int not null auto_increment primary KEY,
	tname VARCHAR(20) not null DEFAULT '江湖',
	email varchar(30) not null DEFAULT '123456',
	gender varchar(4) not null DEFAULT '男')ENGINE=INNODB charset=utf8;

	set auto_num = 1;
	while auto_num <=100000 do
	insert into big_table(tname,email) values((select concat('江湖',auto_num)),(select CONCAT('123456',auto_num,'qq.com')));
	set auto_num=auto_num+1;
	end while;
end //
delimiter;

call insert_t();
insert into big_table(tname,email) values((select concat('江湖',1)),(select CONCAT('123456',1,'qq.com')));
select count(1) from big_table;



--
-- DELIMITER $$
-- DROP PROCEDURE IF EXISTS `proc_auto_insertdata`$$
-- CREATE PROCEDURE `proc_auto_insertdata`()
-- BEGIN
--
--         DECLARE init_data INTEGER DEFAULT 1;
--
--         WHILE init_data <= 10000 DO
--
--         INSERT INTO t_1 VALUES(init_data, CONCAT('测试', init_data), init_data + 10);
--
--         SET init_data = init_data + 1;
--
--         END WHILE;
-- END$$
-- DELIMITER ;
-- CALL proc_auto_insertdata();


'''