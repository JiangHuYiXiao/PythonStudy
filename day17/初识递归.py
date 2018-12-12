#-*- coding:utf-8 -*-
# 递归函数：指的是函数内部调用函数本身
# import sys
# sys.setrecursionlimit(100000) # 设置最大递归深度为100000
# def story():
#     print('从前有座山')
#     story()   # 调用函数本身
#     print('1122')  # 永远不会执行
#
# # 调用函数
# story()   # 循环执行print（‘从前有座山’）

# 但是执行到一定地方会报错，（RecursionError: maximum recursion depth exceeded while calling a Python object）
# 这个地方叫做递归深度，默认递归深度为998或者997，是python从节约内存的角度进行限制的
# import sys
# sys.setrecursionlimit(100000) # 设置最大递归深度为100000
# n = 0
# def story():
#     global n
#     n = n +1
#     print(n)
#     story()
# story()   #
#
# # 可以手动修改默认的递归深度值
# import sys
# sys.setrecursionlimit(100000) # 设置最大递归深度为100000，但是不一定能到100000，和电脑配置有关，我的电脑最大为3926

# 递归总结：
#     如果递归次数太多，就不适合用递归来解决问题
#     递归的缺点：占用内存
#     递归的优点：代码简单

# 求年龄的小例子：使用递归

# alex多大？         n = 1,age(1)
# alex比egon大两岁   age(1) = age(2) + 2
# egon多大？         n = 2 age(2)
# egon比wusir大两岁  age(2) = age(3) + 2
# wusir多大？        n = 3 age(3)
# wusir比金老板大两岁 age(3) = age(4) + 2
# 金老板多大？        n =4 age(4) = 40
# 金老板40了
def age_func(n):
    if n == 4:
        return 40
    elif n >= 1 and n <= 3:
        return age_func(n+1) + 2
        # 这一行，age_func（)先执行，n =1执行就是调用age_func(2),n =2然后再执行age_func(3),n=3然后再执行age_func(4),然后再执行n==4，返回40给age_func（4)---这一步是递
        # 然后再执行40+2，返回给age_func（3)，然后再执行42+2返回给age_func（2)，然后再执行44+2返回给age_func（1)---这一步是归
        # 1     2       3       4
        # 4     3       2       1

print(age_func(1))