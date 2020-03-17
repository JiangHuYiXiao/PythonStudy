# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/3/17 16:49
# @Software       : Python_study
# @Python_verison : 3.7

# Python中使用%还是format来格式化字符串的区别？
# 1、Python新版本推荐使用format
# 2、Python2.6新加入的foramat语法支持
# 3、Python3.6加入了一个f_string新特性
# 4、%格式化时必须写成数组的形式，否则报TypeErrory: not all arguments converted during string formatting
# 定义一个坐标值
# c = (250, 250)
# 使用%来格式化
# s1 = "敌人坐标：%s" % c

# 必须写成这种格式：
# 定义一个坐标值
c = (250, 250)
# 使用%丑陋的格式化...
s1 = "敌人坐标：%s" % (c,)