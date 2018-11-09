# -*- coding:utf-8 -*-
# 一、命名空间
# a、内置命名空间
#      作用时间：在启动python解释器的时候就加载到内存中。
#      包含：if，print，while，for，def 等内置函数
# b、全局命名空间
#       作用时间：是在程序从上到下被执行的过程加载到内存里面
#       包含:函数外部定义的变量名，函数名，等
# c、局部命名空间
#       作用时间：在函数内部定义的变量，当函数调用的时候加载到内存里，随着函数的调用结束而结束。
#       包含:函数内部定义的变量名，函数名，等

a = 1  #全局命名空间包含  a，func
def func(b):
    b = b + 2 #局部命名空间  b
    return b
print(func(1))

# 他们三者从大到小范围是内置命名空间，全局命名空间，局部命名空间，小范围的底层的可以使用上层的，直到找到最近的第一个为止
# 局部命名空间可以使用局部命名空间和内置命名空间和全局命名空间的变量，先使用局部的
# 全局命名空间可以使用全局命名空间和内置命名空间的变量，先使用全局的
# 内置命名空间只可以使用内置空间的变量

# 1、局部命名空间使用内置命名空间和全局命名空间的变量
a = 1
def func(b):
    return max(a,b)   #使用内置命名空间max，和全局命名空间a

print(func(2))

# 2、局部命名空间使用局部命名空间的变量
a = 1
def func(b):
    c = 3
    return max(a,b,c)     #使用局部命名空间c

print(func(2))

# 3、全局命名空间不能使用局部命名空间的变量
a = 1
def func(b):
    c = 3
    return max(a,b,c)
print(c)      #不能使用局部命名空间c
print(func(2))

# 4、全局命名空间使用全局命名空间的变量
a = 1
def func(b):
    c = 3
    return max(a,b,c)
print(a)      #使用全局命名空间a
print(func(2))

# 5、全局命名空间使用内置命名空间的变量
a = 1
def func(b):
    c = 3
print(max(a,2))      #使用内置命名空间max
print(func(2))

# 6、如果在局部命名空间里面没有该变量则找该局部命名空间上一层的最近的第一个为止。
a = 1
def outer(b):
    a = 2
    def inner1():
        print(a)
    inner1()
print(outer(2))   # 2

a = 1
def outer(b):
    def inner1():
        print(a)
    inner1()
print(outer(2))   # 1

# 7、全局命名空间可以使用全局命名空间的变量和内置命名空间的变量，不过先使用全局命名空间的，如果全局找不到再去找内置命名空间的

def input():
    print('my_input')
input()    # my_input

def input1():
    print('my_input')
input()    # 提示输入，使用内置命名空间的input

# 8、局部命名空间可以使用局部命名空间的变量和全局的，以及内置的，但是先使用局部命名空间的变量
a = 1
def max(a,b):
    a = 200
    print(a)
max(1,2)     # 200

def input():
    print('in put now')
def func():
    input()
func()   # in put now   局部的input先找局部没有找到则找全局的，全局找到了则不会再往上找内置的

# 9、每一个函数都有自己的局部命名空间，不同局部命名空间是不能共享的
def func1():
    a = 1

def func2():
    print(a)   #报错每一个函数都有自己的局部命名空间，不同局部命名空间是不能共享的



# 二、作用域
# 1、全局作用域：在全局都可以使用，全局命名空间和内置命名空间的名字属于全局作用域
# 2、局部作用域：在局部使用，局部命名空间的名字属于局部作用域(函数)

a = 1        # a 的作用域就是全局作用域
def func(s):
    print(a)
func(12)


# 3、在局部不能对不可变数据类型，进行值的修改，如果要修改需要在变量前加上nonlocal
a = 1
def func(b):
    a = a+1

# 4、global    全局变量
# 在局部命名空间中，不能对全局作用域的不可变数据类型进行修改操作，但是可以查看，
# 如果想要修改必须在变量名上加上global关键字
# 加上global后，这个变量在局部命名空间修改了，则只会影响全局命名空间的使用该变量的地方
# 一般不建议去在局部命名空间使用global，这样会导致在不知道的情况下变量发生改变
a = 1
def func(b):
    global a
    a = a+1
    return a
print(func(22))    # 2 这个是局部作用域的a
print(a)           # 2 这个是全局命名空间的全局作用域的 a 变量

a = 1
def func(a):
    a = 2
    return a

a = func(a)
print(a)    # 返回2，这样说明在经过函数func的处理后，a的值发生该变了，这样比使用global a 更安全





# 4、想要知道全局作用域或者局部作用域的所有变量globals（），locals（）
# globals永远返回全局的变量
# locals返回的是什么变量取决于放在什么位置，在全局就是全局变量，在局部就是局部变量
a = 1
b = 2
def func():
    x = 'aa'
    y = 'bb'
    print(locals())      #返回局部作用域的{'x': 'aa', 'y': 'bb'}
func()


a = 1
b = 2
def func():
    x = 'aa'
    y = 'bb'
    print(globals())     # 返回全局+内置的变量
func()

a = 1
b = 2
def func():
    x = 'aa'
    y = 'bb'
func()
print(globals())    # 返回全局的变量
print(locals())   # 返回全局的变量，locals放在全局命名空间就是全局作用域的所有变量包含内置的，放在局部命名空间，返回的就是局部作用域的所有变量

a = 1
b = 2
def func():
    x = 'aa'
    y = 'bb'
    print(globals())  # 返回全局的变量
    print(locals())   # 返回局部的变量
func()



# 三、 函数调用：
# func（） 或者 函数的内存地址（）使用这两个都可以
# 函数的名字指向的就是函数的内存地址，我们使用函数名（）进行调用函数时，实际上是通过函数名找到地址，然后根据地址再去执行函数体
a = 1
def func(s):
    print(a)
func(12)
print(func)

# 四、函数嵌套：
# 1、函数嵌套调用
def max(a,b):
    return a if a>b else b

def max3(x,y,z):
    c = max(x,y)    #嵌套调用了上面一个自定义函数max（）
    print(c)        #嵌套调用了内置函数print（）
    return c if c > z else z
print(max(1,3))
print(max3(2,3,5))

# 2、函数嵌套定义

def func():
    print('jianghu')
    def func1():      #func1只是定义了但是没有调用，所以不会执行print('yixiao')
        print('yixiao')
func()                #jianghu


# 让func1产生作用，调用则需要在func里面调用func1
def func():
    print('jianghu')
    def func1():      #func1只是定义了但是没有调用，所以不会执行print('yixiao')
        print('yixiao')
    func1()
func()                #jianghu ,yixiao


# 五 、作用域链

# 在内部函数使用变量的时候，是先从小局部到--->大局部--->全局--->内置的过程，一层一层往上找，找到最近一个就使用，这就是作用域
# 在函数嵌套定义时，内部函数可以使用外部函数的变量，因为内部变量是被完全包含在外部函数的局部命名空间里面
def func():
    a = 1
    def func1():

        print(a)

        def func2():
            print('func2')
        func2()     # 先定义后调用，
    func1()
func()                #1
                      #func2



# 最里面的第三层可以调用外面函数的（二层，一层）的变量,
def func():
    a = 1
    def func1():
        b = 2
        print(a)
        def func2():
            print(a,b)
        func2()     # 先定义后调用，
    func1()
func()                #1,1 ,2


# 只能查看不能修改，
def func():
    a = 1
    def func1():
        b = 2
        print(a)
        def func2():
            # a =a +1    # 报错，只能查看，不能修改
            print(a,b)
        func2()     # 先定义后调用，
    func1()
func()                #1,1 ,2

# 如果想要内部修改的这个变量在外部生效，则需要使用nonlocal关键字
# nonlocal，可以用于改变局部命名空间的局部变量，
# 且声明了nonlocal的内部函数的变量修改，只会影响到离当前函数最近的局部变量
def f1():
    a = 1
    def f2():
        nonlocal a
        a = 2
    f2()
    print('a in f1 : ',a)

f1()

a = 1
def outer():
    a = 1
    def inner():
        a = 2
        def inner2():
            a +=1  #不可变数据类型修改,不支持，需要加上nonlocal
        inner2()
        print('inner2的a:',a)
    inner()
    print('inner1的a:', a)
outer()
print('全局变量a:',a)


a = 1
def outer():
    a = 2
    def inner():
        a = 3
        def inner2():
            nonlocal a  # 声明了一个上面一层的局部变量a，这个a只会影响最近的局部变量，不影响全局变量，全局变量用global
            a +=1  #不可变数据类型修改,不支持，需要加上nonlocal
        inner2()
        print('inner2的a:',a)   # 4  取inner的a取最近的
    inner()
    print('inner1的a:', a)  # 2
outer()
print('全局变量a:',a)   # 1

# 六、函数名的实质
# 1、实质是内存地址
def func():
    pass
print(func)   # <function func at 0x0000000001FA9E18>
# 2、可以赋值
def func1():
    print('func1')
func2 = func1
print(func2)   # <function func1 at 0x0000000001FC9E18>

# 3、可以作为参数传递
def func():
    print('函数')
def func2(a):
    a()
func2(func)     # 函数

# 4、可以作为容器(字典，列表，元组，集合)元素
def func():
    print('函数')
def func2():
    print('hanshu2')
l = [func,func2]
for i in l:
    i()
    # 函数
    # hanshu2

# 5、函数名可以作为返回值
def func():
    print('函数')
def func2(a):
    a()
    return a
jianghu = func2(func)     # 函数
jianghu()                 # 函数



# 七、闭包

# 1、闭包必须是嵌套函数，且内部函数必须调用了外部函数的变量
a = 1
def outer():
    a = 100
    def inner():   # inner()就是一个闭包函数
        print(a)

outer()

'''
由于有了作用域的关系，我们就不能拿到函数内部的变量和函数了。如果我们就是想拿怎么办呢？返回呀！
我们都知道函数内的变量我们要想在函数外部用，可以直接返回这个变量，那么如果我们想在函数外部调用函数内部的函数呢？
是不是直接就把这个函数的名字返回就好了？
这才是闭包函数最常用的用法
'''
# 2、函数外部，使用内部函数的变量,只需要在内部函数返回变量
a = 1
def func(args):
    b = 2
    return b
c = func(21) + 2
print(c)
print(a)

# # 3、函数外部调用函数内部的函数,只需要返回函数名
def outer():
    name = 'jianghu'
    def inner():
        print(name)
    return inner
res = outer()
res()

# 4、判断闭包函数发的方法，函数.__closure__
a = 1
def outer():
    a = 100
    def inner():   # inner()就是一个闭包函数
        print(a)
    print(inner.__closure__)
outer()     # (<cell at 0x00000000027D06D8: int object at 0x000007FED91FE080>,),有cell则是闭包，否则不是


a = 1
def outer():
    a = 100
    def inner():
        print('jianghu')
    print(inner.__closure__)
outer()     # None  不是闭包

# 5、闭包嵌套

def outer():
    money = 1000
    def func():
        name = 'jianghu'
        def inner():
            print(name,money)
        return inner
    return func
func_id = outer()
inner_id = func_id()
inner_id()   #外部使用内部函数


# 6、闭包网络应用
# 返回网站的html文件
from urllib.request import urlopen
res = urlopen('https://www.cnblogs.com/Eva-J/p/7277026.html').read()
print(res)

# 写成函数
from urllib.request import urlopen
def get_url():
    url = 'https://www.cnblogs.com/Eva-J/p/7277026.html'
    res = urlopen(url).read()
    print(res)
get_url()    #这样每次调用都要重新创建一个url，浪费资源

# 所以需要改成闭包格式，我们可以直接在外部使用内部函数，不过内部函数需要有返回值
from urllib.request import urlopen
def get_url():
    url = 'https://www.cnblogs.com/Eva-J/p/7277026.html'
    def innner():
        res = urlopen(url).read()
        print(res)
    return innner

inner_id = get_url()
inner_id()   #这样每次调用inner函数时不需要每次创建url对象