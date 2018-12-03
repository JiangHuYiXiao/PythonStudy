#-*- coding:utf-8 -*-

# 面试题1、看代码写结果
def demo():
    for i in range(4):
        yield i

g = demo()
g1 = (i for i in g)
g2 = (i for i in g1)

print(list(g1))    # [0,1,2,3]
print(list(g2))


def demo():
    for i in range(4):
        yield i

g = demo()
g1 = (i for i in g)

g2 = (i for i in g1)

print(list(g1))    # [0,1,2,3]
print(list(g2))    #[]   分析：因为g1去g中取到0到3的值给了list，g2再去g1中取值，但是g1中没有了，所以g1也不会再去g中取值，g的值都给了g1


# 面试题2：看代码写结果

def add(n,i):
    return n+i
def test():
    for i in range(4):
        yield i

g = test()
for n in [1,10]:
    g = (add(n,i) for i in g)
print(list(g))

# 以后遇到for循环里面为生成器表达式时就把源代码注释掉，一步一步来
# 上面的程序可以简化为
def add(n,i):               # 定义的时候不执行
    return n+i
def test():                 # 定义的时候不执行
    for i in range(4):
        yield i
g = test()
# for n in [1,10]:
#     g = (add(n,i) for i in g)
n = 1
g = (add(n,i) for i in test())   # 定义的时候不执行
n =10
g = (add(n,i) for i in (add(n,i) for i in test()))   # 定义的时候不执行

print(list(g))              # 这个时候才执行

# 分析过程
# g = (add(n,i) for i in (add(n,i) for i in (0,1,2,3)))
# g = (add(n,i) for i in (10+(0,1,2,3))
# g = (10+ (10+(0,1,2,3))
# g = (20,21,22,23)
# list(g)=[20,21,22,23]

# 面试题扩展，看代码写结果
def add(n,i):
    return n+i
def test():
    for i in range(4):
        yield i

g = test()
for n in [1,10,5]:
    g = (add(n,i) for i in g)
print(list(g))

# 分析过程：
# 执行到print(list(g))后才去调用生成器函数，生成器表达式，普通函数
# n = 1
# g = (add(n,i) for i in g)
# n = 10
# g = (add(n,i) for i in g)
# n = 5
# g = (add(n,i) for i in g)

# 最后一步步执行下来最终为
# n = 1
# g = (add(n,i) for i in test())
# n = 10
# g = (add(n,i) for i in (add(n,i) for i in test()))
# n = 5
# g = (add(n,i) for i in (add(n,i) for i in (add(n,i) for i in test())))
# g = (add(n,i) for i in (add(n,i) for i in (5+(0,1,2,3))
# g = (add(n,i) for i in (5+ (5,6,7,8)
# g = (5+ (5+ (5,6,7,8)
# g= (15,16,17,18)
# list(g) = [15,16,17,18]
