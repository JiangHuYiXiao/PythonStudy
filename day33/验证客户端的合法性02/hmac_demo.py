# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/9/25 8:26
# @Software       : Python_study
# @Python_verison : 3.7

import hmac
# 创建hmac对象
# h = hmac.new()  # secret_key 和你想进行加密的bytes类型的数据
# 密文 = h.digest()
# hmac().compare_digest()  对比，客户端的密文和服务端的密文是否一致