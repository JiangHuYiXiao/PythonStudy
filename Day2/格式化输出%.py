# -*- coding:utf-8 -*-
'''
格式化输出：按照特定格式输出数据
使用%号进行占位，然后%加上s或者d代表占位的需要输出的数据类型，
%s代表占位的数据，数据类型为字符串
%d代表占位的数据，数据类型为数字
'''

# 例子：使用格式化输出下面信息
'''
-----------info of jianghuyixiao----------
name ：jianghuyixiao
age  ：27
height：172
job：IT
----------------END-----------------------
'''
name = input('请输入你的姓名：')
age = int(input('请输入你的年龄：'))
height = input('请输入你的身高：')
job =input('请输入你的工作：')
msg = '''
-----------info of %s----------
name : %s
age : %d
height :%s
job : %s
--------------END--------------''' %(name,name,age,height,job)
#age ： %d 这里也可以使用%s替换，以后我们工作中尽量使用%s一般都不会出错
print(msg)

# 如果需要输出%，则需要两个%%，第一个代表转义，第二个代表%

sex = input('请输入你的性别：')
percent = input('请输入你的学习进度：')
info = 'sex : %s percent : %%%s' %(sex,percent)
print(info)




