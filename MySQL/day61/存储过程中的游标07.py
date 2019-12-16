# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/12/16 20:55
# @Software       : Python_study
# @Python_verison : 3.7
'''
-- 8、存储过程中的游标
-- mysql中的游标使用的场景是当我们需要对表中的每一行数据进行操作时，可以使用游标进行操作

-- 需求：一个表的数据来源与另一个表的数据
-- A.ID + A.NUM = B.NUMBER

delimiter //
create PROCEDURE p7()

BEGIN
	declare row_id int;
	declare row_num int;
	declare done int DEFAULT FALSE;
	declare sum_number int;

	declare my_cursor cursor for select id,num from A;
	declare CONTINUE HANDLER for not FOUND set done=TRUE;

	open my_cursor;
		jianghu: loop
		FETCH my_cursor into row_id,row_num;
		if done then
			LEAVE jianghu;
		end if;
		set sum_number = row_id + row_num;
		insert into B(number) VALUES(sum_number);
		end loop jianghu;
	close my_cursor;

end //
delimiter;
drop PROCEDURE p7;
call p7();

'''