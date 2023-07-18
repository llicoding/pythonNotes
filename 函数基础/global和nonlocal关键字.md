# global关键字
修改全局作用域中变量
```python
x = 1

def f1():
    x = 2
    def f2():
        #         global x  # 修改全局
        x = 3
    f2()

f1()
print(x)
```
```python
x = 1
``
def f1():
    x = 2

    def f2():
        global x  # 修改全局
        x = 3
    f2()

f1()
print(x)
```
# nonlocal关键字
```python
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
```
```python
x = 1

def f1():
    x = 2

    def f2():
        nonlocal x
        x = 3

    f2()
    print(x)

f1()
```
