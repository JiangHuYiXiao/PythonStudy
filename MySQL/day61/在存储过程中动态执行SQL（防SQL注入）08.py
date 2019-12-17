# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/12/17 8:21
# @Software       : Python_study
# @Python_verison : 3.7
'''
-- 10、存储过程中动态执行SQL语句，防止SQL注入
delimiter //
create PROCEDURE p8(
in nid int
)
BEGIN
set @hu = nid;
prepare jianghu from 'select * from t_student where s_id>?';			-- 检测sql是否合法
EXECUTE jianghu USING @hu;			-- sql格式化
DEALLOCATE PREPARE jianghu;			-- 执行sql

END //
delimiter ;
call p8(10);

drop PROCEDURE p8;
'''