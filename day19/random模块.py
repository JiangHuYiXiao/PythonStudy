# -*- coding:utf-8 -*-
'''
import random
# 1、随机小数
print(random.random())          # 0.03246672633430814  返回一个大于0小于1之间的小数

print(random.uniform(1,3))    # 2.064717947407578 返回大于1小于3的随机小数
# 2、随机整数
print(random.randint(1,5))      # 5 返回大于1小于等于5直接的随机整数

print(random.randrange(1,10,2))      # 7 返回大于1小于10直接的奇数

# 3、随机选择列表中的一个返回
print(random.choice([1,2,[231,3242],'2oqu']))

# 4、随机选择列表中的多个返回，返回的个数取决于第二个参数的值
print(random.sample([231,3242,'12'],3))         # [231, 3242, '12']
print(random.sample([231,3242,'12'],2))         # ['12', 3242]
print(random.sample([231,3242,'12'],1))         # [231]

# 5、打乱列表的顺序
item = [1,2,3,4,5,6]
random.shuffle(item)
print(item)         # [2, 5, 6, 4, 3, 1]
'''
# 练习：验证码
# print(chr(65))
# print(ord('A'))

import random
def v_code():
    code = ''
    for i in range(5):
        num=random.randint(0,9)
        alf=chr(random.randint(65,90))
        add=random.choice([num,alf])
        code="".join([code,str(add)])
    return code
print(v_code())
