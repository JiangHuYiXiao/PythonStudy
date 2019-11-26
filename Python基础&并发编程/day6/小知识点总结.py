# -*- coding:utf-8 -*-
# python2和python3的区别

# 1、编码方式
# python2，默认不支持中文
# python3，默认支持中文

# 2、打印
# python2不需要使用括号，
# python3需要使用括号

# 3、用户输入
# python2中，是使用raw_input
# python3中，是使用input

# 4、有序列表
# python2中，有xrange和range
# python3中，只有range


# =，==，id三者有啥区别
# 1、=:   是赋值运算符
# 2、==： 是比较运算符
# 3、id： 是比较两个变量的内存地址是否一致
a = 1
b = a
print(id(a),id(b))     #8791505753120 8791505753120
print(a is b)          #True

# 针对不同的数据类型，id有如下规律
# 不可变数据类型int，str
# python3中存在一个小数据池的概念，为了节省内存，只针对于不可变数据类型，可变数据类型是没有如下规律的，
# int：（如果int范围是-5到256，则a和b的id一致，否则id不一致）
a1 = 12
b1 = 12
print(a1 is b1)  #True

a2 = 300
b2 = 300
print(a2 is b2)  #False
# str：
# 1、如果有特殊字符则，不会共用一个内存地址
# 2、如果a*num（num小于21则是同一个内存地址，大于等于则是不同内存地址）
a22 = 'a@'
b22 = 'a@'
print(a22 is b22)  #False   pycharm中无法体现，需要在命令窗口中输入


a3 = 'a'
b3 = 'a'
print(a3 is b3)  #True

a4 = 'a*21'
b4 = 'a*21'
print(a4 is b4)   #False