```python
# []内可以有多个任意类型的值，逗号分隔元素
# my_girl_friend = list(['jason','tank','sean'])
my_girl_friend = ['jason', 'tank', 'sean']

print(f"my_girl_friend: {my_girl_friend}")

l = list('hello nick')
print(f"l: {l}")
```
1. 按索引取值（正向取值+反向取值），即可存也可以取
```python
# list之索引取值
name_list = ['nick', 'jason', 'tank', 'sean']
name_list[0] = 'nick handsom'
# name_list[1000] = 'tank sb'  # 报错

print(f"name_list[0]: {name_list[0]}")
print(f"name_list[0]: {name_list[1]}")
print(f"name_list[0]: {name_list[1]}")
```
2. 切片
```python
# list之切片
name_list = ['nick', 'jason', 'tank', 'sean']

print(f"name_list[0:3:2]: {name_list[0:3:2]}")
```
3. 长度
```python
# list之长度
name_list = ['nick', 'jason', 'tank', 'sean']

print(f"len(name_list): {len(name_list)}")
```
4. 成员运算in和not in
```python
# list之成员运算in和not in
name_list = ['nick', 'jason', 'tank', 'sean']

print(f"'tank sb' in name_list: {'tank sb' in name_list}")
print(f"'nick handsome' not in name_list: {'nick handsome' not in name_list}")
```
5. 追加值
```python
# list之追加值
name_list = ['nick', 'jason', 'tank', 'sean']
name_list.append('tank sb')

print(f"name_list: {name_list}")
```
6. 删除

```python
# list之删除
name_list = ['nick', 'jason', 'tank', 'sean']
del name_list[2]

print(f"name_list: {name_list}")
```
7. 循环
```python
# list之循环
name_list = ['nick', 'jason', 'tank', 'sean']

for name in name_list:
    print(name)
```

```python
# list之insert()
name_list = ['nick', 'jason', 'tank', 'sean']
name_list.insert(1, 'handsome')

print(f"name_list: {name_list}")
```
```python
# list之pop()，pop()默认删除最后一个元素
name_list = ['nick', 'jason', 'tank', 'sean']

print(f"name_list.pop(1): {name_list.pop(1)}")
print(f"name_list: {name_list}")
```
```python
# list之remove()
name_list = ['nick', 'jason', 'tank', 'sean']

print(f"name_list.remove('nick'): {name_list.remove('nick')}")
print(f"name_list: {name_list}")
```
```python
# list之count()
name_list = ['nick', 'jason', 'tank', 'sean']

print(f"name_list.count('nick'): {name_list.count('nick')}")
```
```python
# list之index()
name_list = ['nick', 'jason', 'tank', 'sean']

print(f"name_list.index('nick'): {name_list.index('nick')}")
```
```python
# list之clear()
name_list = ['nick', 'jason', 'tank', 'sean']
name_list.clear()

print(f"name_list: {name_list}")
```
```python
# list之copy()
name_list = ['nick', 'jason', 'tank', 'sean']

print(f"name_list.copy(): {name_list.copy()}")
```
```python
# list之extend()
name_list = ['nick', 'jason', 'tank', 'sean']
name_list2 = ['nick handsome']
name_list.extend(name_list2)

print(f"name_list: {name_list}")
```
```python
# list之reverse()
name_list = ['nick', 'jason', 'tank', 'sean']
name_list.reverse()

print(f"name_list: {name_list}")
```
```python
# list之sort()，使用sort列表的元素必须是同类型的
name_list = ['nick', 'jason', 'tank', 'sean']
name_list.sort()

print(f"name_list: {name_list}")

name_list.sort(reverse=True)
print(f"name_list_reverse: {name_list}")
```