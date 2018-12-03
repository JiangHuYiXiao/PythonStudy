#-*- coding:utf-8 -*-
# 1、处理文件，用户指定要查找的文件和内容，将文件中包含要查找的内容的每一行都输出到屏幕。
# def search_generator():
#     with open('python',mode='r+',encoding='utf-8') as file:
#         for i in file:
#             if 'Python' in i:
#                 yield i
#
# g = search_generator()
# for i in g:
#     print(i)

def search_generator():
    with open('python',mode='r+',encoding='utf-8') as file:
        res = [i.strip() for i in file if 'Python' in i]
        return res

g = search_generator()
print(g)


# 2、写生成器，从文件中读取内容，在每一次读取到的内容之前加上‘***’之后再返回给用户。