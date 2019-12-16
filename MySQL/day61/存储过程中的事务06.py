# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/12/16 20:18
# @Software       : Python_study
# @Python_verison : 3.7
'''
-- 7、存储过程中的事务
delimiter //
create PROCEDURE p6(
out status int
)
begin
declare exit HANDLER for SQLEXCEPTION
begin
-- error
	set status = 1;
	ROLLBACK;
end;
start TRANSACTION;
	insert into t1(NAME) VALUES('zhazha');
commit;
-- success
set status = 2;
END //
delimiter;

set @v1=0
call p6(@v1);
select @v1;
'''