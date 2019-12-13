# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/12/13 15:04
# @Software       : Python_study
# @Python_verison : 3.7
'''
-- 存储过程：是一个SQL语句的集合；

-- 1、创建简单的存储过程
delimiter //
create PROCEDURE P1()
BEGIN
select * from t_student;
insert into t_teacher(tname) VALUES('yixiu');
end //
delimiter ;

-- 2、调用存储过程
call p1


-- 3、有参数的存储过程（in）in表示入参
delimiter//
create PROCEDURE p2(
in arg1 int,
in arg2 int
)
BEGIN
select * from t_student where s_id=arg1;
insert into t_teacher(tname) VALUES('yixiu');
end //
delimiter ;

call p2(12,2)

-- 3、删除存储过程
drop PROCEDURE p2;


-- 5、有参数的存储过程（out）out表示返回值
delimiter//
create PROCEDURE p3(
in arg1 int,
out arg2 int
)
BEGIN
set arg2=123;
select * from t_student where s_id=arg1;
insert into t_teacher(tname) VALUES('yixiu');
end //
delimiter ;



-- 先设置变量v1
set @v1 = 0;
-- 调用存储过程
call p3(12,@v1)

-- 查询变量值
select @v1;



-- 6、有参数的存储过程（inout）表示入参和返回值
drop PROCEDURE if EXISTS p4;
delimiter//
create PROCEDURE p4(
inout arg1 int

)
BEGIN
set arg1=12;
select * from t_student where s_id=arg1;
insert into t_teacher(tname) VALUES('yixiu');

end //
delimiter ;



-- 先设置变量v1
set @v2 = 0;
-- 调用存储过程
call p4(@v2);

-- 查询变量值
select @v2;


# 7、使用pymysql操作简单的存储过程
import pymysql
conn = pymysql.connect(host='127.0.0.1',user='root',password='',database='db1',charset='utf8')
cursor = conn.cursor()
# 调用存储过程
cursor.callproc('p1')
res = cursor.fetchall()
print(res)
conn.commit()
cursor.close()
conn.close()

# 8、使用pymysql操作带in参数的存储过程
import pymysql
conn = pymysql.connect(host='127.0.0.1',user='root',password='',database='db1',charset='utf8')
cursor = conn.cursor()
# 调用存储过程
cursor.callproc('p2',(12,3))            # 传参数
res = cursor.fetchall()
print(res)
conn.commit()
cursor.close()
conn.close()
'''


# 9、使用pymysql操作带out参数的存储过程
import pymysql
conn = pymysql.connect(host='127.0.0.1',user='root',password='',database='db1',charset='utf8')
cursor = conn.cursor()

# 调用存储过程
cursor.callproc('p3',(12,3))            # 传参数
# 拿结果集
res1 = cursor.fetchall()
print(res1)


# 拿返回值out的
cursor.execute('select @_p3_0,@_p3_1')
res2 = cursor.fetchall()
print(res2)
conn.commit()
cursor.close()
conn.close()

# 总结存储过程的特性：存储过程有返回值（out，inout），可以传参数
# 实际应用存储过程：
#     存储过程中有out、inout返回值，是为了当我们执行sql语句时，返回执行结果，判断存储过程是否执行成功。