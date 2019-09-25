# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/9/4 9:09
# @Software       : PythonStudy
# @Python_verison : 3.7
# 摘要算法（md5，sha）的应用
#     1、登录验证
#     2、加密，解密
#     3、文件比对
#     4、字符串比对

# 注册时候使用摘要算法得出一个唯一的值，然后登陆的时候再次使用摘要算法，然后比较两者的结果是否一致，
# 这就是为啥现在的忘记密码功能都是重置密码，而不是直接返回给你密码。
#不管算法多么不同，摘要的结果一致，使用同一个摘要算法得出的结果肯定是一致的。
# 使用不同的算法得出的结果应该是不同的。
'''


# 实际登录例子
# 注册
import hashlib
h = hashlib.md5()
h.update(b'123456')         # 必须是字节类型的
pwd = h.hexdigest()         # 转化为16进制的结果
print(pwd)

h = hashlib.md5()
h.update(b'jianghu')
user = h.hexdigest()
print(user)

# 登录
import hashlib
input_username = input('请输入用户名：')
input_password = input('请输入密码：')
with open('userinfo')as file:
    for line in file:
        password,username = line.split('|')
    md51 = hashlib.md5()
    md51.update(bytes(input_username,encoding = 'utf-8'))
    user = md51.hexdigest()
    md52 = hashlib.md5()
    md52.update(bytes(input_password,encoding = 'utf-8'))
    pwd = md52.hexdigest()
    print(user,pwd)
    if user == username and pwd == password:
        print('登录成功')
    else:
        print('登录失败,用户名或者密码错误')

# 所谓撞库就是从别的渠道搞了一堆用户名和密码，拿到另外的网络服务器，一个一个的往里试用户名和密码，恰好对了，这就叫撞库
# 为了防止撞库，我们可以对上面的代码进行加盐处理

# 加盐
import hashlib
h = hashlib.md5(bytes('盐',encoding='utf-8'))
h.update(b'jianghu')            # 1e96f616dbeda20c6d50f69af939435b
user = h.hexdigest()
print(user)         # 6b6429a834dbb43e0c80175f52d31e94


# 动态加盐
# 使用用户名的一部分
import hashlib
h = hashlib.md5(bytes('盐',encoding='utf-8'+username[1:3]))
h.update(b'jianghu')            # 1e96f616dbeda20c6d50f69af939435b
user = h.hexdigest()
print(user)         # 6b6429a834dbb43e0c80175f52d31e94
'''

# 文件的一致性校验，是不需要加盐处理的，一般用分步进行摘要，其摘要的结果和一次性摘要是一样的
import hashlib
md5 = hashlib.md5()       # 创建一个md5对象
md5.update(b'123')
md5.update(b'456')
print(md5.hexdigest())    # e10adc3949ba59abbe56e057f20f883e