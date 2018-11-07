#-*- coding:utf-8 -*-
# 1、写函数，检查获取传入列表或者元组对象所有奇数的位索引对应的元素，并将其作为新列表返回给调用者。
'''
方法1：
def func(*args):
    list = []
    for i in args:
        index = args.index(i)
        if index % 2 == 1:
            list.append(i)
    return list
# 调用函数
res = func(2,3,1,5,6,9,4)
print(res)

res = func(*[1,3,5,6,7])
print(res)

# 方法2：
def func(args):
    list = []
    for i in args:
        index = args.index(i)
        if index % 2 == 1:
            list.append(i)
    return list

# 方法3：
def func(args):
    return args[1::2]

# 调用函数
res = func((2,3,1,5,6,9,4))
print(res)

res = func([1,3,5,6,7])
print(res)
'''
# 2、写函数，判断用户传入的对象（字符串，列表，元组）长度是否大于5
'''
# 方法1：
def func2(args):
    k = 0
    for i in args:
        k += 1
    if k > 5:
        return True
    else:
        return False
res1 = func2('sdjfoiwe')
res2 = func2('sd')
res3 = func2([1,2,43,543])
res4 = func2([1,2,3,4,5,6])
res5 = func2((1,2,3,4,5,6,7))
print(res1,res2,res3,res4,res5)

# 方法2：
def func(args):
    return(len(args) > 5)   #这里尽量都用return不用print或者break，这样因为有返回值，我们可以再对返回值做操作
print(func('abcd'))
if func('abcdd6'):
    print('对象的长度确实大于5')
'''
# 3、写函数，检查传入列表的长度，如果大于2，那么保留前两个长度的内容，并将新内容返回给调用者。
'''
# 方法1
def func3(list):
    lis = []
    k = 0
    for i in list:
        k += 1
    # if k <= 2:
    #     return
    if k > 2:
        lis.append(list[0])
        lis.append(list[1])
        return lis
    else:
        return
res1 = func3([113,12,33,44])
res2 = func3([113,12])
print(res1,res2)

# 方法2:*************简化版***************
def func(li):
    if len(li) >2:
        return li[:2]
print(func([1,2,3,4]))

# 方法2:*************精华版*************
def func(li):
        return li[:2]
print(func([1,2,3,4]))
'''

# 4、写函数，计算传入字符串中的数字，字母，空格，以及其他的个数，并返回结果。
'''
def func4(arg):
    i =0
    s =0
    space =0
    other =0
    for k in arg:
        if k.isdigit():
            i = i + 1
        if k.isalpha():
            s = s + 1
        if k.isspace():
            space = space + 1
    other = len(arg)-i-s-space
    return(i,s,space,other)
print(func4('12ww @#'))
'''
# 5、写函数，检查用户传入的对象（字符串，列表，元组），检查用户传入的每一个元素是否含有空内容，并返回结果。
'''
def func5(kwargs):
    k = 0
    for i in kwargs:

        if i.isspace():
            k += 1
            print(True)
    return k
# print(func5(str1 = 'intw 32',list1 =[1,3, '',32],tuple1 =(1,3,'')))
print(func5('123  3'))
print(func5([1,3, '',32]))
'''

# 6、写函数，检查传入字典的每一个value的长度，如果大于2，那么保留前两个长度的内容，并将新内容返回给调用者。
# 字典的value值只能是字符串或者列表
'''
def func6(args):
    dic = {'k1': 'v1v2', 'k2': [11, 22, 33, 44]}
    list = []
    for i in dic.values():
        if len(i) > 2:
            list.append(i[0])
            list.append(i[1])
    return list
res = func6({'k1': 'v1v2', 'k2': [11, 22, 33, 44]})
print(res)
'''
# 7、接收两个数字参数，返回较大的数
'''
# def compare_large(a,b):
#     if a > b:
#         return a
#     if a < b:
#         return b
#     else:
#         print('两个数一样大')
# print(compare_large(2,1))
'''

# 8、写函数，用户传入修改的文件名，与要修改的内容，执行函数，完成整个文件的批量修改操作。

# def replace_func(name,content):
#     with open('name',mode='r+',encoding='utf-8') as file,open('replace_name',mode='w+',encoding='utf-8') as replace_file:
#         for line in file:
#             line = line.replace('alex','SB')
#             replace_file.write(line)
# import os
# os.remove('name')
# os.replace('replace_name','name')


# 9、写一个函数，完成三次注册，再写一个函数完成三次登录
'''
# 1、定义函数
def registe():
    sum_digit = 0
    sum_lower = 0
    sum_upper = 0
    for i in range(3):

        # 2、输入用户名
        name = input('请输入用户名:用户名必须包含数字、小写字母、大写字母且数字不能开头，字符长度为8-16个字符')
        for i in name:
            if i.isupper():
                sum_upper += 1
            if i.islower():
                sum_lower += 1
            if i.isdigit():
                sum_digit += 1
        if (sum_digit <=0 or sum_digit > 6) or (sum_lower <=0 or sum_digit > 6) or (sum_upper <=0 or sum_digit > 6):
            print('用户名必须包含数字、小写字母、大写字母且数字不能开头，字符长度为8 - 16个字符')
            break
        if name[0].isdigit():
            print('数字不能开头，请重新输入用户名！')
            break
        if len(name) < 8 or len(name) > 16:
            print('用户名字符长度为8-16个字符，请重新输入用户名！')
            break

        #3、输入密码
        password = input('请输入密码:密码必须包含数字、小写字母、大写字母且数字不能开头，字符长度为6-8个字符')
        for i in password:
            if i.isupper():
                sum_upper += 1
            if i.islower():
                sum_lower += 1
            if i.isdigit():
                sum_digit += 1
        if (sum_digit <=0 or sum_digit > 6) or (sum_lower <=0 or sum_digit > 6) or (sum_upper <=0 or sum_digit > 6):
            print('密码必须包含数字、小写字母、大写字母且数字不能开头，请重新输入密码！')
            break
        if password[0].isdigit():
            print('数字不能开头，请重新输入密码！')
            break
        if (len(password) < 6) or (len(password) > 8):
            print('密码长度为6-8个字符，请重新输入密码！')
            break
        # 4、注册成功
        else:
            print('恭喜你，注册成功！')

        # 5、将用户名，密码写入注册信息文件中，分行写入
        with open('注册信息',mode='w+',encoding='utf-8') as file:
            file.write('{}\n{}'.format(name,password))
        return
registe()

def login():
    for i in range(3):
        list = []
        login_name = input('请输入你的登录用户名：')
        login_password = input('请输入你的密码：')
        with open('注册信息', mode='r+', encoding='utf-8') as file:
            for line in file:
                list.append(line)
            if list[0].strip() == login_name.strip() and list[1].strip() == login_password.strip():
                print('恭喜你，登录成功！')
                break
            else:
                print('用户名或者密码错误，请重新登录！')
    print('三次机会已经用完，请明天再来！')
login()
'''