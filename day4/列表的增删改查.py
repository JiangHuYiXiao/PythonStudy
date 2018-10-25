# -*- coding:utf-8 -*-
'''
li = ['jianghu','jiangxi','Rose','Jack']

# 1、列表索引
L1 =li[0]
print(L1)
L5 = li[-1]
print(L5)
# 2、列表切片
L2 = li[0:3]
print(L2)
L3 = li[0:]
print(L3)
L4 = li[:]
print(L4)
#3、倒序
L7 = li[3:0:-1]
print(L7)
L8 = li[::-1]
print(L8)

#4、列表的增加
# 第一种：append()在列表的后面追加li
#****列表的操作都是在原有列表上进行操作，不像str在新的字符串上操作。***
li.append('polo')
print(li)
# 需求：在一个员工列表中不断增加元素，但是输入Q就会退出

#V1
li = ['jianghu','jiangxi','Rose','Jack']
while 1:
        name = input('请输入增加的员工:')
        if name == 'Q':
            break
        else:
            li.append(name)
print(li)

#V2,Q不区分大小写，且去除前后空格

li = ['jianghu','jiangxi','Rose','Jack']
while 1:
    name = input('请输入增加的员工:')
    if name.strip().upper() == 'Q':
        break
    else:
        li.append(name)
print(li)

# 第二种：insert  在指定索引位置插入元素
li.insert(0,'what')
print(li)

# 第三种：extend,迭代添加，在最后位置
li.extend('jianghu')
print(li)
# li.extend(123) #TypeError: 'int' object is not iterable
print(li)
li.extend([1,2,3])
print(li)

# 5、列表的删除

# 第一种：pop，指定索引进行删除，不指定索引时默认删除最后一个，有返回值，返回值就是删除的那个元素

li.pop(1)  
print(li)

li.pop()
print(li)

# 第二种：remove,通过指定元素去删除
li.remove('jianghu')
print(li)

li.remove('jinagd')  #ValueError: list.remove(x): x not in list
print(li)

# 第三种：clear，清空列表。列表元素为空
li.clear()
print(li)

# 6、列表的修改

li[0] = 'jiangjiang'
print(li)

li[0:2] = 'jianghu'  # 列表的修改都是把原先的元素删除，然后把新的加入进去，按照一个元素一个元素添加
print(li)  # ['j', 'i', 'a', 'n', 'g', 'h', 'u', 'Rose', 'Jack']

# 7、列表的查找

# 按照索引去查
print(li[1])

# 按照切片去查
print(li[0:2])
print(li[:])

# 使用for循环去查
for i in li:
    print(i)

# 8、其他方法
# 统计字符串出现的次数count
print(li.count('jianghu'))
print(li.count('12'))

# 计算列表的长度
print(len(li))

# 返回元素的索引值
print(li.index('jianghu'))
# print(li.index('jiagn'))   ValueError: 'jiagn' is not in list

#反转
li.reverse()
print(li)

# 对列表进行排序sort,效率最高的排序
# 正向排序
list = [1,34,5,7,77]
list.sort()
print(list)
'''
# 如果元素是字符串，则按照字符串的首字母的ascii的十进制进行排序
list1 = ['ab','jiang','cd','js','python']
list1.sort()
print(list1)
print(str(ord('a')) + '--'+'--' + str(ord('b')) + '--' + ' --' + str(ord('c')))
print(str(ord('A')) + '--' + str(ord('B')))

# 倒序排序
# list.sort(reverse=True)
# print(list)