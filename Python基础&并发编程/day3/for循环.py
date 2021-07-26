# -*- coding:utf-8 -*-
'''
for循环是有限循环，while循环是无限循环(不知道循环次数用while)
for i in s:  (i是变量，s是可迭代对象，可迭代对象指的是里面包含的元素众多，
            像123就不是可迭代对象，'jianghu'就是可迭代对象，我们后面讲的：列表、元组、字典、集合都是包含多个元素，所以是可迭代对象)
    循环体
'''
for i in 'jianghuyixiao':
    print(i)


# 1~10之间的奇数
for i in range(1,10,2):
    print(i)

# 1~10之间的奇偶数
for i in range(2,11,2):
    print(i)