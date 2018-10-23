#-*- coding:utf-8 -*-

# 索引：就是字符串中字符的位置，索引开始值为0
str = 'ABCdddfoeghicd'
s1 = str[0]  #s1是一个新的字符串，与str没有任何关系,只是生成一个新的字符串，旧的字符串不变。
print(s1)
print(str[2])
# 取最后一位
print(str[-1])
print(str[-2])
# 切片
s2 = str[0:2]  #取出第一个到第二个 #顾头不顾尾
print(s2)

#取第一位到最后一位
print(str[:])
print(str[0:])
print(str[::1])
print(str[0::1])

# 按照步伐间隔的取,默认不填写时步伐为1
print(str[0:7:2])

# 倒序取并且倒序输出
print(str[4:0:-1])  #ddCB
print(str[4::-1])    #ddCBA

# 倒序间隔着取
print(str[4::-2])   #dCA

# 倒序取整个字符串
print(str[-1::-1])
print(str[::-1])


