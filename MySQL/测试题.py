# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/11/26 16:32
# @Software       : Python_study
# @Python_verison : 3.7
'''

/*创建表t_classs表*/
CREATE TABLE t_class (
	class_id INT auto_increment PRIMARY KEY,
	caption VARCHAR (20) NOT NULL
) ENGINE = INNODB DEFAULT charset = utf8;

/*插入数据*/
insert into t_class(class_id,caption) values(1,'三年二班');
insert into t_class(caption) values('一年三班');
insert into t_class(caption) values('三年一班');

/*查询*/
select * from t_class;

delete FROM t_class;


/*创建表t_teacher表*/
CREATE TABLE t_teacher (
	teacher_id INT auto_increment PRIMARY KEY,
	tname VARCHAR (18) NOT NULL
) ENGINE = INNODB DEFAULT CHARSET = utf8;

drop table t_techer;

insert INTO t_teacher(teacher_id,tname) values(1,'波多');
insert INTO t_teacher(tname) values('苍空');
insert INTO t_teacher(tname) values('饭岛');

select * from t_teacher;


/*创建表t_student表*/







CREATE TABLE t_student (
	s_id auto_increment PRIMARY KEY,
	sname VARCHAR (20) NOT NULL,
	gender CHAR (2) NOT NULL,
	CONSTRAINT fk_student_class FOREIGN KEY ('s_class_id',) REFERENCES t_class (class_id)
) ENGINE = INNODB DEFAULT CHARSET = utf8;
一、创建表

/*创建表t_classs表*/
CREATE TABLE t_class (
	class_id INT auto_increment PRIMARY KEY,
	caption VARCHAR (20) NOT NULL
) ENGINE = INNODB DEFAULT charset = utf8;

/*插入数据*/
insert into t_class(class_id,caption) values(1,'三年二班');
insert into t_class(caption) values('一年三班');
insert into t_class(caption) values('三年一班');
insert into t_class values(2,'一年二班'),(3,'一年三班');

/*查询*/
select * from t_class;

delete FROM t_class;


/*创建表t_teacher表*/
CREATE TABLE t_teacher (
	teacher_id INT auto_increment PRIMARY KEY,
	tname VARCHAR (18) NOT NULL
) ENGINE = INNODB DEFAULT CHARSET = utf8;

drop table t_techer;

insert INTO t_teacher(teacher_id,tname) values(1,'波多');
insert INTO t_teacher(tname) values('苍空');
insert INTO t_teacher(tname) values('饭岛');

select * from t_teacher;


/*创建表t_student表*/
DROP TABLE
IF EXISTS t_student;
CREATE TABLE t_student (
	s_id INT auto_increment PRIMARY KEY,
	sname VARCHAR (20) NOT NULL,
	gender CHAR (2) NOT NULL,
	s_class_id INT NOT NULL,
-- 	KEY fk_student_class ('s_class_id'),
	CONSTRAINT fk_student_class FOREIGN KEY (s_class_id) REFERENCES t_class (class_id)
) ENGINE = INNODB DEFAULT CHARSET = utf8;

INSERT INTO t_student(s_id,sname,gender,s_class_id) VALUES(1,'钢蛋','女',1);
INSERT INTO t_student VALUES(2,'铁锤','女',1),(3,'山炮','男',2);COMMIT;
select * from t_student;



-- 创建课程表t_course
DROP TABLE
IF EXISTS t_course;
CREATE TABLE t_course (
	course_id INT auto_increment PRIMARY KEY,
	course_name CHAR (10) NOT NULL,
	c_teacher_id INT NOT NULL,
	CONSTRAINT fk_course_teacher FOREIGN KEY (c_teacher_id) REFERENCES t_teacher (teacher_id)
) ENGINE = INNODB DEFAULT CHARSET = utf8;

insert into t_course values(1,'生物',1),(2,'体育',1),(3,'物理',2);
select * from t_course;


-- 创建成绩表t_score
DROP TABLE
IF EXISTS t_score;
CREATE TABLE t_score (
	score_id INT auto_increment PRIMARY KEY,
	score_student_id INT NOT NULL,
	score_course_id INT NOT NULL,
	score_number INT NOT NULL,
	unique uq(score_student_id,score_course_id),
	CONSTRAINT fk_score_student FOREIGN KEY (score_student_id) REFERENCES t_student (s_id),
	CONSTRAINT fk_score_course FOREIGN KEY (score_course_id) REFERENCES t_course (course_id)

) ENGINE = INNODB auto_increment=1 DEFAULT CHARSET = utf8;


-- 插入数据
insert INTO t_score values(1,1,1,60),(2,1,2,59),(3,2,2,100);
insert INTO t_score(score_student_id,score_course_id,score_number) values(1,1,6);

-- 查询数据
select * from t_score;

二、操作表

1、自行创建测试数据

2、查询“生物”课程比“物理”课程成绩高的所有学生的学号；

3、查询平均成绩大于60分的同学的学号和平均成绩；

4、查询所有同学的学号、姓名、选课数、总成绩；

5、查询姓“李”的老师的个数；

6、查询没学过“叶平”老师课的同学的学号、姓名；

7、查询学过“001”并且也学过编号“002”课程的同学的学号、姓名；

8、查询学过“叶平”老师所教的所有课的同学的学号、姓名；

9、查询课程编号“002”的成绩比课程编号“001”课程低的所有同学的学号、姓名；

10、查询有课程成绩小于60分的同学的学号、姓名；

11、查询没有学全所有课的同学的学号、姓名；

12、查询至少有一门课与学号为“001”的同学所学相同的同学的学号和姓名；

13、查询至少学过学号为“001”同学所选课程中任意一门课的其他同学学号和姓名；

14、查询和“002”号的同学学习的课程完全相同的其他同学学号和姓名；

15、删除学习“叶平”老师课的SC表记录；

16、向SC表中插入一些记录，这些记录要求符合以下条件：①没有上过编号“002”课程的同学学号；②插入“002”号课程的平均成绩；

17、按平均成绩从低到高显示所有学生的“语文”、“数学”、“英语”三门的课程成绩，按如下形式显示： 学生ID, 语文, 数学, 英语, 有效课程数, 有效平均分；

18、查询各科成绩最高和最低的分：以如下形式显示：课程ID，最高分，最低分；

19、按各科平均成绩从低到高和及格率的百分数从高到低顺序；

20、课程平均分从高到低显示（现实任课老师）；

21、查询各科成绩前三名的记录: (不考虑成绩并列情况)

22、查询每门课程被选修的学生数；

23、查询出只选修了一门课程的全部学生的学号和姓名；

24、查询男生、女生的人数；

25、查询姓“张”的学生名单；

26、查询同名同姓学生名单，并统计同名人数；

27、查询每门课程的平均成绩，结果按平均成绩升序排列，平均成绩相同时，按课程号降序排列；

28、查询平均成绩大于85的所有学生的学号、姓名和平均成绩；

29、查询课程名称为“数学”，且分数低于60的学生姓名和分数；

30、查询课程编号为003且课程成绩在80分以上的学生的学号和姓名；

31、求选了课程的学生人数

32、查询选修“杨艳”老师所授课程的学生中，成绩最高的学生姓名及其成绩；

33、查询各个课程及相应的选修人数；

34、查询不同课程但成绩相同的学生的学号、课程号、学生成绩；

35、查询每门课程成绩最好的前两名；

36、检索至少选修两门课程的学生学号；

37、查询全部学生都选修的课程的课程号和课程名；

38、查询没学过“叶平”老师讲授的任一门课程的学生姓名；

39、查询两门以上不及格课程的同学的学号及其平均成绩；

40、检索“004”课程分数小于60，按分数降序排列的同学学号；

41、删除“002”同学的“001”课程的成绩；

'''