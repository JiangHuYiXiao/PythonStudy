#-*- coding:utf-8 -*-
# 文件处理
'''
一、打开文件
# 1、相对路径：当前目录
# 2、绝对路径：根目录
# 3、文件操作的模式：r，rb，r+，w，wb，w+，a，ab，a+，不指定模式，默认是读方式
    # r：只读，只能进行读，不能进行多余的任何一步操作
    # rb：只读，以bytes类型进行操作，不需要指明编码方式（针对于视频，图片，用这种模式操作）
    # r+:可读，可写
    # 1、先写，后读:先写是把文件原有内容替换，写多少替换多少，再读
    # 2、先读，后写:先读后，则光标是在最后位置，再写的话，则是在后面追加

    # w：只写
    # wb：以bytes类型进行写
    # w+：可写，可读
    # 先写后读：写模式都是把原先内容全部删除，后再写，然后再读

    # a：追加：在文件后面追加
    # ab：以bytes类型进行追加
    #a+：可写，可读
'''
# 二、操作文件
# 读
# read :一次性读
# readline  ：一行一行读
# readlines ：一次性读，按照行切分，放列表中
# 最好的方法：
# for line in file:
#     pass

# 4、文件操作方式
# 文件操作的第1种方式：
f = open('文件操作相对路径',mode='r+',encoding='utf-8')
re = f.read()
f.write('江湖一笑')

# 三、关闭文件
f.close()

# 文件操作的第2种方式：open是系统命令，告诉操作系统需要打开文件
with open('文件操作相对路径',mode='r+',encoding='utf-8') as file:
    re1 = file.read()
    file.write('追加')
# 以后常用是第二种，且模式一般都是r+

# 5、文件操作的常用方法
# file.tell()             # 返回光标的位置
# file.seek(1)            # 调节光标位置
# file.readable()         # 是否可读
# file.readline()         # 一行一行读
# file.readlines()        # 一次全部读整个文件
# file.truncate()         # 对文件进行截取

# 6、读文件，全部读，一行一行，打印，每行中间换行
with open('文件操作相对路径', mode='r+', encoding='utf-8') as file1:
    for i in file1:          # 循环读文件，一行一行读
        print(i)
# 四、修改文件
# 7、文件的修改,默认python中没有文件修改的方法，需要间接去修改
# 逻辑：读源文件，把源文件内容写到新的文件，然后删除文件，重命名新文件
# 把源文件中的行，替换成列
# 方法1
with open('源文件',mode='r+',encoding='utf-8')as source_file,open('新文件',mode='w+',encoding='utf-8')as replace_file:
    for line in source_file:
        if '列'in line:
            line = line.replace('列','行')
        replace_file.write(line)
import os
os.remove('源文件')
os.rename('新文件','源文件')

# 方法2：在内存中修改文件
import os    # 导入os模块，该模块是用于文件操作的
with open('源文件',mode='r+',encoding='utf-8')as source_file,open('替换文件',mode='w+',encoding='utf-8') as replace_file:
    data = source_file.read()
    data = data.replace('行','列')
    replace_file.write(data)
os.remove('源文件')
os.replace('替换文件','源文件')

# 方法3：每一行读出来然后进行替换
import os
with open('源文件',mode='r+',encoding='utf-8')as source_file,open('替换文件',mode='w+',encoding='utf-8') as replace_file:
    for line in source_file:
        line1 = line.replace('列','行')
        replace_file.write(line1)
os.remove('源文件')
os.replace('替换文件','源文件')


