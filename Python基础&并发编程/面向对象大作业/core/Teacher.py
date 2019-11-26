#-*- coding:utf-8 -*-

# 学校类
class School:
    def __init__(self,school_name,address):
        self.name = school_name
        self.address = address
        self.classmate = [python1,python2,go1,go2,linux1,linux2]
S1 = School('江湖一笑','北京')

# 班级类
class Classmate:
    def __init__(self,classmate_name,school,kind,):
        self.classmate_name = classmate_name
        self.school = school
        self.kind = kind
        self.student =[jianghu,jiangxi,jiangge,jianghao,jiangchi,jianghe]
python1 = Classmate('python1','北京','python')
python2 = Classmate('python1','上海','python')
go1 = Classmate('go1','北京','go')
go2 = Classmate('go2','上海','go')
linux1 = Classmate('linux1','北京','linux')
linux2 = Classmate('linux2','上海','linux')

# 课程类
class Course:
    def __init__(self,course_name,period,price):
        self.course_name =course_name
        self.period = period
        self.price = price
C1 = Course('python','6month',18000)


# 老师类
class Teacher:
    def __init__(self,teacher_name):
        self.teacher_name = teacher_name
        self.classmate = [python1,python2]
        self.course = C1            # 组合



# 学生类
class Student:
    def __init__(self,student_name):
        self.student_name = student_name
        self.classmate = [python1, python2, go1, go2, linux1, linux2]

jianghu = Student('jianghu')
jiangxi = Student('jiangxi')
jiangge = Student('jiangge')
jianghao = Student('jianghao')
jiangchi = Student('jiangchi')
jianghe = Student('jianghe')
