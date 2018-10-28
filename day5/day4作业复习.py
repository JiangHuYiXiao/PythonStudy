# -*- coding:utf-8 -*-

# 5、查找列表li中的元素，移除每个元素的空格，     ----对字符串进行去空格
# 并找出以’A’或者’a’开头，并以’c’结尾的所有元素，----找出字符串
# 并添加到一个新列表中,最后循环打印这个新列表。----字符串添加到新列表
# li = [‘taibai ’,’alexC’,’AbC ’,’egon’,’ Ritian’,’ Wusir’,’  aqc’]

'''
# 方法1：

li = ['taibai ','alexC','Abc ','egon','Ritian',' Wusir','  aqc']
new_li = []
for i in li:
    if (i.strip().startswith('A') or i.strip().startswith('a')) and i.strip().endswith('c'):
        s = i.strip()
        new_li.append(s)

print(new_li)
'''

# 方法2：
'''
li = ['taibai ','alexC','Abc ','egon','Ritian',' Wusir','  aqc']
new_li = []
for i in li:
    if i.strip()[0].upper() == 'A' and i.strip()[-1] == 'c':
        new_li.append(i.strip())
print(new_li)
'''

# 方法3：
'''

li = ['taibai ','alexC','Abc ','egon','Ritian',' Wusir','  aqc']
new_li = []
for i in li:
    if (i.strip()[0].startswith('a') or i.strip()[0].startswith('A')) and i.strip()[-1].endswith('c'):
        new_li.append(i.strip())
print(new_li)
'''


# 6、开发敏感词语过滤程序，提示用户输入评论内容，如果用户输入的内容中包含特殊的字符：
# 敏感词列表 li = ["苍老师","东京热",”武藤兰”,”波多野结衣”]
# 则将用户输入的内容中的敏感词汇替换成***，并添加到一个列表中；
# 如果用户输入的内容没有敏感词汇，则直接添加到上述的列表中。

li = ['苍老师','东京热','武藤兰','波多野结衣']
new_li = []
info = input('请输入你的评论内容：')
for i in li:   #先小范围，
    if i in info:    #再判断小范围在不在大范围里面，因为我们输入的肯定要包含小范围的，否则不替换
        num = len(i)
        info = info.replace(i,'*'*num)
new_li.append(info)

print(new_li)

