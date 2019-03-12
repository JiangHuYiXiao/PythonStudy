# -*- coding:utf-8 -*-
'''
角色:
学校、学员、课程、讲师

要求:
1. 创建北京、上海 2 所学校

2. 创建linux , python , go 3个课程 ， linux\py 在北京开， go 在上海开

3. 课程包含，周期，价格

4. 班级关联课程、讲师

5. 创建学员时，选择学校，关联班级

5. 创建讲师角色时要关联学校

6. 提供三个角色视图

　　6.1 学员视图， 登陆， 查看课程、查看班级

　　6.2 讲师视图， 讲师可查看自己教学的班级、课程。

　　　　　　　　　 进阶需求：可管理自己的班级， 查看班级学员列表 ， 修改所管理的学员的成绩

　　6.3 管理视图，创建讲师， 创建班级，创建课程

7. 上面的操作产生的数据都通过pickle序列化保存到文件里
'''
# 学校类
class School:
    def __init__(self,school_name,address,classmate):
        self.name = school_name
        self.address = address
        self.classmate = classmate

# 老师类
class Teacher(School):
    def __init__(self,teacher_name,kind):
        self.name = teacher_name
        self.kind = kind

# 课程类
class Course:
    def __int__(self,course_name,period,price):
        self.course_name =course_name
        self.period = period
        self.price = price

# 班级类
class Classmate(Course,Teacher):
    def __init__(self,classmate_name,):
        self.classmate_name = classmate_name


# 学生类
class Student(School):
    def __init__(self,student_name):
        self.student_name = student_name
    # 登录
    def login(self):
        input_name = input('请输入账号：')
        input_password = input('请输入密码：')


# 创建学校对象
S1 = School('go_school','上海',['go1','go2','go3'])
S2 = School('linux_python_school','北京',['python1','linux2','linux3'])

