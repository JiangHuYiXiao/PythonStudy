# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/12/12 19:42
# @Software       : Python_study
# @Python_verison : 3.7
'''


-- 触发器：
-- 		是为了我们在进行数据库的增删改时，可以在增删改查前后进行其他关联的操作

-- 1、触发器创建
-- 创建（插入的，其他删除、修改是一样的操作）
create trigger t BEFORE insert on t_student for EACH ROW
BEGIN
insert into t_teacher(teacher_id,tname) values(6,'jianghu');
END

-- 删除
drop trigger t;

show triggers like 't_student';
desc t_student;
desc t_teacher;

-- 触发
insert into t_student(gender,s_class_id,sname) values('女',1,'小龙女');


-- New 表示新插入的数据 (只有insert 、update才有new)
create trigger t BEFORE insert on t_student for EACH ROW
BEGIN
insert into t_teacher(teacher_id,tname) values(new.s_id,new.sname);
END

-- 触发
insert into t_student(s_id,gender,s_class_id,sname) values(28,'女',3,'小龙女');


-- old 表示旧的数据 (delete，update才有old)
create trigger t BEFORE delete on t_student for EACH ROW
BEGIN
insert into t_teacher(teacher_id,tname) values(old.s_id,old.sname);
END

delete from t_student where s_id=17;
'''