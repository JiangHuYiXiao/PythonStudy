#-*- coding:utf-8 -*-

# 1、三目运算符
# 成立的结果 if 条件成立 else 条件不成立的结果

# 2、send的效果和next一样都可以取值的，但是send可接收值用于下一个yield
    # 第一次使用生成器的时候是首先用next获取值
    # send不能用在最后一个yield进行取值

# 2.1普通的生成器函数
# 定义一个生成器函数

def generator():
    print('a')
    yield 1
    print('b')
    yield 2
    print('c')
    yield 3
# 调用一个生成器函数
g = generator()         # 返回一个生成器

# 生成器取值，通过next
print(g.__next__())

# 生成器取值，通过for循环
for i in g:
    print(i)

# 2.2最后一个没有yield的生成器函数
def generator():
    print('a')
    yield 1
    print('b')
    yield 2
    print('c')
    # yield 3   #最后没有yield，c是可以正常返回的，但是会报错StopIteration

# 调用一个生成器函数
g = generator()         # 返回一个生成器
g1 = generator()
# 生成器取值，通过next
print(g.__next__())
print(g.__next__())
print(g.__next__())    # StopIteration

# 2.3send调用，可以接收值，且可以返回
def generator():        # 步骤1
    print('a')          # 步骤4
    content = yield 1   # 右边步骤5  左边步骤7
    print('=======',content)        # 步骤 8
    print('b')        # 步骤 9
    yield 2        # 步骤 10


# 调用一个生成器函数
g = generator()         # 返回一个生成器   步骤2

# 生成器取值，通过next
print(g.__next__())         # 步骤3
print(g.send('hello world'))   # 不能在第一个位置   # 步骤6


# 2.4最后一个如果yiel后面还有代码，需要执行，想使用send，则在可以在最后代码后面加一个yield，返回值为空
def generator():        # 步骤1
    print('a')          # 步骤4
    content = yield 1   # 右边步骤5  左边步骤7
    print('=======',content)        # 步骤 8
    print('b')        # 步骤 9
    yield 2        # 步骤 10
    '其他代码'
    yield

# 调用一个生成器函数
g = generator()         # 返回一个生成器   步骤2

# 生成器取值，通过next
print(g.__next__())         # 步骤3
print(g.send('hello world'))   # 不能在第一个位置   # 步骤6


#
# 3、移动平均值
# 推到过程1
def average1():
    sum = 0
    count = 0
    avg = 0
    while True:     # 这样是为了循环取值，取多个
        num = yield     # 这里写yield是为了接收传过来的num，但是num怎么传呢，可以通过参数，或者send,
                        # 但是这里因为是有yield，所以只能通过send
        sum += num
        count += 1
        avg = sum / count
        yield avg    # 需要再返回avg要不然报错，且我们无法取到值

# 生成器取值
avg_g = average1()
avg_g.__next__()
print(avg_g.send(10))
avg_g.__next__()
print(avg_g.send(20))
avg_g.__next__()
print(avg_g.send(30))
# 这个推到过程有个问题就是每次都需要执行next，send，next，send，......,
# 关键是next执行只是为了激活生成器，没有值返回，为了是下一步send能够接收值


# 推导过程2
def average2():
    sum = 0
    count = 0
    avg = 0
    while True:     # 这样是为了循环取值，取多个
        # num = yield     # 这里写yield是为了接收传过来的num，但是num怎么传呢，可以通过参数，或者send,
        #                 # 但是这里因为是有yield，所以只能通过send
        num = yield avg  # 进入循环一开始就取到avg的值,然后还可以避免一开始0/0的bug
        sum += num
        count += 1
        avg = sum / count


# 生成器取值
avg_g = average2()
avg_g.__next__()   # 这个时候这里返回的是0
print(avg_g.send(10))  # 进行到这一步后再把10赋值给num
print(avg_g.send(20))


# 4、预激装饰器的生成器
# 定义一个初始函数init
def init(func):  # func = average
    def inner(*args,**kwargs):

        g = func(*args,**kwargs)   # g是一个生成器
            # 把我们刚刚取生成器函数值需要激活生成器函数的next放在需要计算的函数之后
        g.__next__()
    return inner


@init   # average = init(average)
def average():
    sum = 0
    count = 0
    avg = 0
    while True:     # 这样是为了循环取值，取多个
        num = yield avg  # 进入循环一开始就取到avg的值,然后还可以避免一开始0/0的bug
        sum += num
        count += 1
        avg = sum / count


# 生成器取值
avg_g = average()
print(avg_g.send(10))
print(avg_g.send(20))

# 5、yield from：从一个容器里面一个一个取值

# 需求返回a= ‘abcdef’,b = 12345的每一个字符
# 方法1：
def generator():
    a = 'abcdef'
    b = '12345'
    for i in a:
        yield(i)
    for i in b:
        yield(i)
g = generator()
for i in g:
    print(i)


# 方法2：
def generator():
    a = 'abcdef'
    b = '12345'
    yield from a
    yield from b

g = generator()
for i in g:
    print(i)
