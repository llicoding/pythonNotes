# 可变长形参之*
def sum_self(*args):
    res = 0
    for num in args:
        res += num
    return res


res = sum_self(1, 2, 3, 4)
print(res)

# 可变长实参之*
# def demo_func(*args, b): # 报错，*args可接收各类数据，接收(1, 2 ,100)
def demo_func(b, *args):

    print(args)
    print(b)
    
demo_func(1, 2, 100)

def demo_func(*args, b):

    print(args)
    print(b)
    
demo_func(1, 2, b=100)

# 可变长形参之**
def func(**kwargw):
    print(kwargw)

func(a=5)

# 可变长实参之**
def func(x, y, z, **kwargs):
    print(x, y, z, kwargs)

func(1, 3, 4, **{'a': 1, 'b': 2})

# 函数的嵌套调用
def max2(x, y):
    if x > y:
        return x
    else:
        return y

def max4(a, b, c, d):
    res1 = max2(a, b)
    res2 = max2(res1, c)
    res3 = max2(res2, d)
    return res3

print(max4(1, 2, 3, 4))

# global关键字
# 在局部作用域中对全局变量修改需要用global关键字声明
x = 1

def f1():
    x = 2

    def f2():
        #         global x  # 修改全局
        x = 3
    f2()

f1()
print(x)

x = 1

def f1():
    x = 2

    def f2():
        global x  # 修改全局
        x = 3
    f2()

f1()
print(x)

# nonlocal关键字
# 修改局部作用域中的变量
x = 1

def f1():
    x = 2

    def f2():
        #         nonlocal x
        x = 3

    f2()
    print(x)

f1()

x = 1

def f1():
    x = 2

    def f2():
        nonlocal x
        x = 3

    f2()
    print(x)

f1()