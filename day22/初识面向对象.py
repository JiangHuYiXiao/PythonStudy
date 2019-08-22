# -*- coding:utf-8 -*-
# 面向对象的引入：
    # 人狗大战
'''
# 1、定义人
def Person(name,blood,aggr,sex,):       # ---人模子
    person = {
        'name':name,
        'blood':blood,
        'aggr':aggr,
        'sex':sex
     }
    return person
alex = Person('狗蛋儿',100,1,'不详')
nezha = Person('哪吒',1000,100,'小孩子')
print(alex)
print(nezha)

# 2、定义狗
def Dog(name, blood,aggr,kind):         # ---狗模子
    dog = {
        'name': name,
        'blood': blood,
        'aggr': 100,
        'kind': kind
           }
    return dog
Jin_Dog = Dog('金小狗',10000,10,'teddy')
print(Jin_Dog)

# 这样使得代码精简，然后方便扩展，修改属性，还有属性比较规范
# Person和Dog只是定义了一类事物，直到调用了函数，才有真的人或者狗
# 3、人打狗
def Person_Attack(person,dog):
    dog['blood'] = dog['blood'] - person['aggr']
    print('%s被打了，掉了%s血'%(dog['name'],person['aggr']))

# 4、狗咬人
def Dog_Attack(dog,person):
    person['blood'] = person['blood'] - dog['aggr']
    print('%s被咬了，掉了%s血'%(person['name'],dog['aggr']))

Person_Attack(alex,Jin_Dog)
Dog_Attack(Jin_Dog,alex)
# 会出现一个人咬狗，或者狗打人的问题
Person_Attack(Jin_Dog,alex)   # 出现错乱
'''
# 优化代码
def Person(name,blood,aggr,sex):       # ---人模子
    person = {
        'name':name,
        'blood':blood,
        'aggr':aggr,
        'sex':sex
     }

    def Person_Attack(dog):
        dog['blood'] = dog['blood'] - person['aggr']
        print('%s被打了，掉了:%s滴血' % (dog['name'], person['aggr']))
    person['attack'] = Person_Attack
    return person

def Dog(name, blood,aggr,kind):         # ---狗模子
    dog = {
        'name': name,
        'blood': blood,
        'aggr': aggr,
        'kind': kind
           }
    def Dog_Attack(person):
        person['blood'] = person['blood'] - dog['aggr']
        print('%s被咬了，掉了:%s滴血' % (person['name'], dog['aggr']))
    dog['attack'] = Dog_Attack
    return dog
Jin_Dog = Dog('金小狗',10000,10,'teddy')
Alex_Person = Person('狗蛋儿',100,1,'不详')
print(Alex_Person)  # {'name': '狗蛋儿', 'blood': 100, 'aggr': 1, 'sex': '不详', 'attack': <function Person.<locals>.Person_Attack at 0x00000000022E9048>}Alex_Person这个对象字典中包含了函数Person_Attack
print(Jin_Dog)  # {'name': '金小狗', 'blood': 10000, 'aggr': 10, 'kind': 'teddy', 'attack': <function Dog.<locals>.Dog_Attack at 0x00000000022D8F28>}Jin_Dog这个对象字典中包含了函数Dog_Attack

Alex_Person['attack'](Jin_Dog)
Jin_Dog['attack'](Alex_Person)

# 面向对象编程：
# 模子就是类，类是抽象的，我能知道有什么属性有什么技能，但是不能知道属性具体的值
# Alex_Person，Jin_Dog，nezha就是对象，实际的 有具体的属性值，都是根据类来规范的
# 先有类才有对象