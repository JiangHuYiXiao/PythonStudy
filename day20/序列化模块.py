# -*- coding:utf-8 -*-
# 序列化：就是其他数据类型转换为字符串数据类型的过程。
# 序列化的应用：
#     1、数据存储，文件传输
#     2、网络传输

# 反序列化：字符串数据类型转换回其他数据类型的过程。

# 序列化的几个常用模块：
# 1、json
#     通用的序列化格式
#     但是只有很少的一部分数据类型可以通过json转化成字符串
# json中包含的方法
    # 1、dumps序列化方法，直接操作内存里面的内容
    # 2、loads反序列化方法，直接操作内存里面的内容
    # 3、dump 先把数据类型序列化，然后往文件里面写东西，一般我们往文件里面写东西，只能写字符串，不能写字典、元组等
    # 4、load 通过load方法从文件里面读东西,读取出来的内容数据类型还是写进去的
'''
# dumps
import json
dic = {'k1':'v1'}
dic_str = json.dumps(dic)
print(type(dic_str),dic_str)    # <class 'str'> {"k1": "v1"}
dic_d = json.loads(dic_str)
print(type(dic_d),dic_d)    # <class 'dict'> {'k1': 'v1'}

# loads
# 列表，字典，元组，字符串，数字，都可以进行序列化和反序列化
# 元组
tup = (1,3,4)
tup_str = json.dumps(tup)
print(type(tup_str),tup_str)    # <class 'str'> [1, 3, 4]
tup_l = json.loads(tup_str)
print(type(tup_l),tup_l)    # <class 'list'> [1, 3, 4]

# 集合不可以序列化，也就不可以反序列化
set = {1,3,2}
set_str = json.dumps(set)
print(type(set_str),set_str)    # TypeError: Object of type set is not JSON serializable
set_l = json.loads(set_str)
print(type(set_l),set_l)    # TypeError: Object of type set is not JSON serializable

# dump
import json
dic = {'k1':'v1'}
f = open('file',mode='w',encoding='utf-8')
f.close
json.dump(dic,f)

import json
f = open('file',mode='r',encoding='utf-8')
f.close
res = json.load(f)
print(type(res),res)        # <class 'dict'> {'k1': 'v1'}

import json
dic = {'k1':'我去'}
f = open('file1',mode='w',encoding='utf-8')   # 中文写进文件里面是{"k1": "\u6211\u53bb"}
json.dump(dic,f)
f.close

f1 = open('file1',mode='r',encoding='utf-8')
res = json.load(f1)
print(type(res),res)


import json
dic = {'k1':'我去'}
f1 = open('file1',mode='w',encoding='utf-8')   # 中文写进文件里面是{"k1": "\u6211\u53bb"}
json.dump(dic,f1,ensure_ascii=False)   # 加上ensure_ascii属性


f1 = open('file1',mode='r',encoding='utf-8')        # {"k1": "我去"}
res = json.load(f1)
print(type(res),res)
'''
# json往文件里面写东西和读只能一次性
import json
# dic = {'k':'12','k1':'13'}
# f = open('file2',mode='w',encoding='utf-8')
# json.dump(dic,f)
# json.dump(dic,f)
# f.close()
f = open('file2',mode='r',encoding='utf-8')
res = json.load(f)
res1 = json.load(f)

print(type(res),res,res1)




# 2、pickle
#     所有的python中的数据类型都可以转换成字符串的形式
#     但是pickle序列化的内容只有python可以理解
#     且部分反序列化依赖python代码
# 3、shelve
#     python3新增的模块
#     序列化句柄
#     使用句柄直接操作

