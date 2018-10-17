# -*- coding:utf-8 -*-
'''
一、while循环语句：
while 条件（可以是比较运算，布尔值等）：
    循环体：（需要包含终止循环语句（否则就是死循环）
             终止循环：1、改变条件，使条件不成立
                      2、break  立刻中断跳出循环，不执行while循环了
                      3、continue 中断本次循环，执行下个迭代 ）

'''
# 输出1到100的值。
# 方法1：标志位
count = 0
flag = True
while flag:
    count += 1
    print(count)
    if count == 100:
        flag = False

# 方法2：
count = 0
while count < 100:
    count += 1
    print(count)

'''
循环终止：
1、break ---终止整个循环，执行循环以外的代码。
2、continue---终止本次循环，执行下次循环。
'''
#break
print('break相关demo')
while True:
    print('你')
    break
    print('他')   #不会被执行因为遇到break，终止整个循环。如果没有break，这个循环体会一直执行，死循环
print('人民')

#continue
print('continue相关demo')
a = 0
while a < 10:

    a += 1
    if a == 6:
        continue
      #不会打印6，因为遇到continue，不会执行a==6这次循环，但是还会执行a大于6小于10的循环
    print(a)
print('loop out')

# 作业:
# 1、输出1加到100的值。
# 2、输出1-5和95-100的数据。
# 3、使用while循环输出1、2、3、4、5、7、8、8、9、10.
# 4、输出1-100所有奇数的和
# 5、输出1-100所有偶数的和
# 6、用户登录三次机会
# 作业1、方法1：
count = 1
sum = 0
while count <= 100:
    sum = sum + count
    if count == 100:
        print(sum)
    count += 1

# 作业1、方法2：
count = 1
sum = 0
while count <= 100:
    sum = sum + count
    count += 1
print(sum)

# 作业2:输出1-5和95-100的数据。
a = 0
while a < 100:
    a += 1
    if a > 5 and a < 95:
        continue
    print(a)

# 作业3、使用while循环输出1、2、3、4、5、7、8、8、9、10.
count = 0
while count < 10:
    count += 1
    if count == 6:
        continue
    print(count)   #通过以上几个例子，我们得出规律，如果要在循环输出中不输出某个值，
    # 1、用continue进行终止
    # 2、而且叠加条件（count += 1）需要放在if判断之前，输出结果需要放在if之后

# 4、输出1-100所有奇数的和
count = 0
sum = 0
while count < 100:
    count += 1
    if count % 2 == 1:
        sum += count
print(sum)

# 5、输出1-100所有偶数的和
count = 0
sum = 0
while count <= 100:
    count += 1
    if count % 2 == 0:
        sum += count
print(sum)   #2550

# 6、用户登录三次机会

name1 = 'jianghuyixiao'
password1 = 123123
count = 1
while count <= 3:
    name = input('请输入你的用户名：')
    password = int(input('请输入你的密码：'))
    if name == name1 and password == password1:
        print('恭喜你登录成功')
    else:
        print('用户名或者密码错误，请修改后重新登录！')
    count += 1











