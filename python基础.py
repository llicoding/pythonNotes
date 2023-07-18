# 变量必须由变量名、赋值符号和变量值三部分组成
name = 'nick'
age = 19
gender = 'male'
height = 180
weight = 140

age = 18
height = 185
print(age)
print(height)

# 变量命名驼峰体
AgeOfNick = 19
print(AgeOfNick)

# 变量命名下划线
age_of_nick = 19
print(age_of_nick)


age = 18
salary = 2.1
name = 'nick'

# 三引号内的字符可以换行，单双引号内的字符不可以换行
name1 = '''nick_
test'''
print(name1)

# 字符串只能+、*和逻辑比较
str01 = "lanlan"
str02 = "huahua"
print(str01+str02)

# 字符串只能乘数字
print(str01*10)

# 字符串比较大小，根据ASCII码比较
print(str01>str02)
print(str01<str02)

# 列表+索引
# 列表中的元素可以是任意类型
hobby = "run"
hobby_list = [hobby, 'read', 'sing']
print(hobby_list)
print(hobby_list[1])

# 索引从0开始
hobby_list = ['read', 'run', ['sing', 'play']]
print(hobby_list[2][0])
print(hobby_list[2][1])

# 字典（给列表中的每个元素添加一个描述信息）
# key: value格式 其中key一般为字符串类型，value为任意格式的数据
user_info = {'name': 'nick', 'gender': 'male', 'age': 22,
             'school_info': ['chengdu', 126, 'CS']}
print(user_info)

# 字典的取值不依赖于索引，而是依赖于key
print(user_info['age'])
print(user_info['school_info'])

# user_info['school_info']取到的是列表['chengdu', 126, 'CS']
print(user_info['school_info'][0])

# 字典套字典
user_info = {'name': 'nick', 'gender': 'male', 'age': 22,
             'school_info': {'school_name': 'scu', 'school_age': 127, 'school_address': 'chengdu'}}
print(user_info['school_info']['school_name'])

# 取出第一个学生的名字
students = [
    {'name': 'nick', 'age': 19},
    {'name': 'egon', 'age': 18}
]
print(students[0]['name'])

# 列表中的元素可以是字典，可以是任意类型的数据

# name = input('请输入你的姓名')
# pwd = input('请输入你的密码')

# print(name)
# print(pwd)


name = 'nick'
age = 19
print('My name is '+name+ ' my age is '+str(age))

# 占位符
name = 'nick'
age = 19
print('My name is %s my age is %s'%(name, age))

# format格式化
print('hello {}, you are {}'.format(name, age))
print('{}{}'.format(name, age))
print('{0}{1}{0}'.format(name, age))
print('{str01}{str02}'.format(str01 = name, str02 = str(age)))

# f-String占位符
print(f'hello, {name}, you are {age}')
print(F'hello, {name}, you are {age}')

salary = 6.6666
print(f'{salary:.2f}')

# 算术运算符
print(1 + 2)
x = 10
y = 20
res = x + y
print(res)

# /有零有整除，得到一个浮点型
print(10 / 3)

# 地板除，只取整数部分
print(10 // 3)

# **，幂
print(10**3)

pwd = '123'
print(pwd != '123')
print(pwd == '123')

l1 = [1, 'a', 3]
l2 = [3]
print(l1 < l2)


# 报错，列表比较大小仅限于同一位置的对应的值是相同的类型
try:
    l3 = [1, 3]
    print(l1 < l3)
except Exception as e:
    print(e)

# is和==的区别：
# is用于判断两个变量引用对象是否为同一个(是否在同一块内存空间中)
# ==用于判断引用变量的值是否相等
x = 3
y = x
z = 3
print(f'x is y: {x is y}')
print(f'x == y: {x == y}')

print(f'x is z: {x is z}')
print(f'x == z: {x == z}')
print({x is z})

# 成员运算符
a = 10
b = 20
list = [1, 2, 3, 4, 5]

if (a in list):
    print("变量 a 在 list 中")
else:
    print("变量 a 不在 list 中")

if (b not in list):
    print("变量 b 不在 list 中")
else:
    print("变量 b 在 list 中")

# python具有垃圾回收机制，垃圾不需要手动释放

# if判断
cls = 'human'
gender = 'female'
age = 18

if cls == 'human' and gender == 'female' and age > 16 and age < 22:
    print('开始表白')


if cls == 'human' and gender == 'female' and age > 16 and age < 22:
    print('开始表白')
else:
    print('阿姨好')


if cls == 'human' and gender == 'female' and age > 16 and age < 22:
    print('开始表白')
elif cls == 'human' and gender == 'female' and age > 22 and age < 30:
    print('考虑下')
else:
    print('阿姨好')

# while循环 + break终止当前层的循环
while True:
    print('1')
    print('2')
    break
    print('3')

# break跳出的是循环，而不是if语句
while True:
    str01 = 'lan'
    str02 = 'hua'
    if str01 == 'lan' and str02 =='hua':
        print("全对了！")
        break
    else:
        print("不是兰花")

print("退出了while循环")

# continue终止本次循环，直接进入下一次循环
# 因此将continue放在循环体的最后一步是没有意义的

n = 1
while n < 10:
    if n == 8:
        # 如果注释这一行，n会一直等于8，则会进入死循环
        n += 1  
        continue
    print(n)
    n += 1

while (1):
    print("hello")
    break

# while循环嵌套，如果需要退出循环，需要设置多个break

# tag控制循环退出
# tag控制循环退出
tag = True
while tag:
    name = input('username:')

    if name == 'lan':
        print('login successful')

        while tag:
            cmd = input('请输入你需要的命令：')
            if cmd == 'q':
                tag = False
            print(f'{cmd} 功能执行')
    else:
        print('username or password error')

print('退出了while循环')


# while + else
# else会在while没有被break时才会执行else中的代码
# 在while循环中没有break的情况下,while循环执行完毕后,会执行else语句

n = 1
while n < 3:
    print(n)
    n += 1
else:
    print('else会在while没有被break时才会执行else中的代码')

n = 1
while n < 3:
    print(n)
    n += 1

print('else会在while没有被break时才会执行else中的代码')

n = 1
while n < 3:
    print(n)
    n += 1
    break
else:
    print('else会在while没有被break时才会执行else中的代码')

name_list = ['nick', 'jason', 'tank', 'sean']
n = 0
while n < 4:
    # while n < len(name_list):
    print(name_list[n])
    n += 1

# while循环无法取字典中的数据，因此需要for循环
# 运用for循环取字典中的值，循环的是key
info = {'name': 'nick', 'age': 19}
for item in info:
    # 取出info中的keys
    print(item)
    # 取出info中key对应的值
    print(info[item])
    print(type(item))

    # item已经是key的字符串形式了，不可以再加''
    # print(info['item'])

del list
print(list)
print(list(range(1, 10)))
for i in range(1, 10):
    print(i)

print(type(range(1, 10))) # class: range

# for循环也可以按照索引取值
name_list = ['nick', 'jason', 'tank', 'sean']
for i in range(len(name_list)):
    print(name_list[i])

# for + break
# for循环调出本层循环
name_list = ['nick', 'jason', 'tank', 'sean']
for name in name_list:
    if name == 'jason':
        break
    print(name)

# for + continue
# for循环调出本次循环，进入下一次循环
name_list = ['nick', 'jason', 'tank', 'sean']
for name in name_list:
    if name == 'jason':
        continue
    print(name)

# for循环嵌套
for i in range(3):
    print(f'-----:{i}')
    for j in range(2):
        print(f'*****:{j}')

# for + else(与while + else相同)
# for循环没有break的时候触发else内部代码块
name_list = ['nick', 'jason', 'tank', 'sean']
for name in name_list:
    print(name)
else:
    print('for循环没有被break中断掉')

name_list = ['nick', 'jason', 'tank', 'sean']
for name in name_list:
    print(name)
    break
else:
    print('for循环没有被break中断掉')
    
import time

print("loading",end = '')
for i in range(6):
    print(".", end = '')
    time.sleep(0.2)