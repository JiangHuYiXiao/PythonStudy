# -*- coding:utf-8 -*-
'''
if 条件1：（条件1满足走下面一个Tab后的语句，条件不满足不执行结果语句）
    结果  （缩进进是为了表明下面的语句是在条件1下面，也就是我们所说的作用域）

'''
# 格式1：只有一个条件选择这个条件（一选一）
age = int(input('请输入年龄：'))
if age < 18 :
    print('未成年')

# # 格式2：两个条件选择一个（二选一）
if age < 18:
    print('未成年')
else:
    print('你也不小了，好好努力吧！')


# 格式3：多个条件选择一个（多选一）
if age < 18 and age >0:
    print('未成年')
elif age  >= 18 and age <= 30:
    print('你也不小了，好好努力吧！')
elif age <= 50 and age > 30:
    print('人到中年')
elif age >50 :
    print('好好享受生活!')
else:
    print('你输入的年龄有误，请修改')


# 格式4：if嵌套if
if age < 18 and age >0:
    if age < 7:
        print('好好享受童年')
    else:
        print('好好学习，天天向上')
else:
    print('你也不小了，好好努力吧！')

