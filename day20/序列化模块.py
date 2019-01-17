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
#     json写和读文件只能一次性
# json中包含的方法
    # 1、dumps序列化方法，直接操作内存里面的内容
    # 2、loads反序列化方法，直接操作内存里面的内容
    # 3、dump 先把数据类型序列化，然后往文件里面写东西，一般我们往文件里面写东西，只能写字符串，不能写字典、元组等
    # 4、load 通过load方法从文件里面读东西,读取出来的内容数据类型还是写进去的

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

# json往文件里面写东西和读只能一次性，会很占用内存
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

# 我们一般操作文件都是希望分步写入，分步读取，可以通过其他方式进行分步取
# 1、写：利用json的dumps对数据进行序列化，变成字符串，然后在每个字符串后面加上换行符'{}\n'
# 2、读：一行一行的读
# 3、再通过loads对每一行进行反序列化，成为字典

# 写
import json
l = [{'k1':'11'},{'k2':'12'},{'k3':'13'}]
f = open('file3',mode='w',encoding='utf-8')
for i in l:
    str_dict = json.dumps(i)
    f.write(str_dict+'\n')
f.close

# 读---->读出来为字符串
import json
f = open('file3',mode='r',encoding='utf-8')
for i in f:
    print(i.strip(),type(i))            # {"k1": "11"} <class 'str'>这个还是字符串，我们需要进行下一步，进行反序列化
f.close()

# 读---->读出来为字典
import json
f = open('file3',mode='r',encoding='utf-8')
for i in f:
    dic = json.loads(i.strip())          # {'k1': '11'} <class 'dict'>这个时候就是字典了
    print(dic,type(dic))
f.close()


# 2、pickle
#     所有的python中的数据类型都可以转换成字符串的形式，但是pickle序列化后的为bytes数据类型，loads出来的是可读的数据类型
#     dump和load时需要使用rb模式
#     但是pickle序列化的内容只有python可以理解
#     且部分反序列化依赖python代码
#     可以分步dump和load
import pickle
# dumps
dic = {'k1':'v1'}
dic_str = pickle.dumps(dic)
print(type(dic_str),dic_str)    # <class 'bytes'> b'\x80\x03}q\x00X\x02\x00\x00\x00k1q\x01X\x02\x00\x00\x00v1q\x02s.'二进制
# loads
dic_d = pickle.loads(dic_str)
print(type(dic_d),dic_d)    # <class 'dict'> {'k1': 'v1'}

# dump
# import pickle
# dic = {'k1':'v1'}
# f = open('file4',mode='wb')
# pickle.dump(dic,f)
# f.close()


# load
import pickle
dic = {'k1':'v1'}
f = open('file4',mode='rb')
res = pickle.load(f)
f.close()
print(res)


# pickle分步写读
import pickle
dic1 = {'k1':'v1'}
dic2 = {'k2':'v2'}
f = open('file5',mode='wb')
pickle.dump(dic1,f)
pickle.dump(dic2,f)
f.close()

f = open('file5',mode='rb')
a1 = pickle.load(f)     # {'k1': 'v1'}
a2 = pickle.load(f)     # {'k2': 'v2'}
print(a1)
print(a2)

# 3、shelve
#     python3新增的模块
#     序列化句柄
#     使用句柄直接操作
# shelve只提供了一个open方法给我们，是用key来访问的，使用起来和字典类似
import shelve
f = shelve.open('shelve_file')
f['key'] = {'int':12,'float':9.3,'str':'woqu'}          # 直接对文件句柄操作，就可以存入数据
f.close()

f1 = shelve.open('shelve_file')
res = f1['key']         # 取出数据也只需要直接使用key获取即可，但是如果key不存在则会报错，
f1.close()
print(res)      # {'int': 12, 'float': 9.3, 'str': 'woqu'}  会生成三个文件


# flag = r
f1 = shelve.open('shelve_file',flag='r')   #只读，但是却也可以改，应该是shelve的bug
res = f1['key']
f1.close()
print(res)

# writeback = True
f1 = shelve.open('shelve_file')
print(f1['key'])
f1['key']['dict'] = {'k1':122}  # 添加值，这样是添加不成功的
res = f1['key']
print(res)          # {'int': 12, 'float': 9.3, 'str': 'woqu'}

f1 = shelve.open('shelve_file',writeback=True)
print(f1['key'])
f1['key']['dict'] = {'k1':122}  # 添加值，这样是添加成功的
res = f1['key']
print(res)          # {'int': 12, 'float': 9.3, 'str': 'woqu', 'dict': {'k1': 122}}