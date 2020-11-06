# -*- coding:utf-8 -*-
# 1、数字（int）

a = 2
b = 8
c = a + b
print(a,b,c)
# 通过type()方法可以查看变量属于哪种的数据类型
print(a,type(a))
d = 3.4
# float
print(d,type(d))
# 运算:+ ,-,*,/,%
print(b - a)
print(b * a)
print(b / a)
print(b % a)

# 2、字符串（str）
name = 'jianghu'
print(name,type(name))
# 字符串不能相减、除，但是支持+和*
sex = '男'
print(name + sex)
print(name * 8)

'''
注意1：
多行字符串需要使用三个单引号或者三个双引号
已经存在单引号后，只能使用双引号
'''



'''
注意2：
1、换行符\n：
2、转义符\：\n,默认前面不加转义符的话，就是换行。\\n ,表示\n。忽略转义符只需要在前面加上r\\n,print结果为\\n
3、字符串拼接：使用+号或者使用空格print(a+b),print('a','b')
4、字符串引用：
# 1、使用f'字符串'{}
    a = 'jianghu'
    b = f'yixiao{a}'
    print(b)
    
# 2、使用format格式化
    a = "jianghu"
    c = "shuaige"
    b = "yixiao{}{}"
    print(b.format(a,c))

'''

msg = '''
人生苦短
我要学python
努力
'''
print(msg)
info = "i'm 18 old"
print(info)
# str转换成int通过int函数，但是有个条件是参数必须是数字
str11 = int('11')


# 3、布尔类型bool
print(True,type(True))
