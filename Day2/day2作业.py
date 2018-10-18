# -*- coding:utf-8 -*-
# 1、判断下列逻辑语句为True或者False
# 优先级：() > not > and > or
a = 1 > 1 or 3 < 4  or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6      #True

b = (not 2 > 1 and 3 < 4  or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6)     #False

c = (1 > 2 and 3 < 4  or 4 > 5 and 2 > 1 and 9 < 8 and 4 > 6 or 3 < 2)     #False
print(a,b,c)

# 2、求出下列逻辑语句的值
d = 8 or 3 and 4 or 2 and 0 or 9 and 7           # 8
e = 0 or 2 and 3 and 4 or 6 and 0 or 3           # 4
f = 5 and 9 or 10 and 2 or 3 and 5 or 4 or 5     # 9
print(d,e,f)
#规律：先not后and后not，and 取后面一个值，or取第一个非0的值

# 3、下列的结果是什么？
g = 6 or 2 > 1  # 6
h = 3 or 2 > 1  # 3
i = 0 or 5 < 4  # 0
j = 5 < 4 or 3  #
k = 2 > 1 or 6  #
l = 3 and 2 > 1 #
m = 0 and 3 > 1 #
n = 2 > 1 and 3 #
o = 3 > 1 and 0 #
p = 3 > 1 and 0 or 2 < 3 and 3 and 4 or 3 > 2   #
print(g,h,i,j,k,l,m,n,o,p)