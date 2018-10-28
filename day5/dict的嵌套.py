#-*- coding:utf-8 -*-
dict = {
    'name': ['jianghu','yixiao','wusir'],
    'py9' : {
        'time':'1213',
        'learn_money':19800,
        'address':'fuyong'
    },
    'age':29
}
# 需求1：把age的值改为38
dict['age'] = 38
print(dict)
print(dict['age'])

# 需求2：在name这个键的值下的列表里面追加一个'luck'元素
dict['name'].append('luck')
print(dict)

# 需求3：把yixiao全部变成大写
dict['name'][1] =dict['name'][1].upper()
print(dict)

# 需求4：在py9这个字典下面添加一个键值对
# 方法1：
dict['py9'].setdefault('female',6)
print(dict)

# 方法2
dict['py9']['female'] = 6
print(dict)


dict['py9'].append('feamale',8)  # 失败，字典下面没有append方法
print(dict)

