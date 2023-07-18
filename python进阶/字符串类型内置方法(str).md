# 字符串类型内置方法(str)
``` python
name = 'nick'
s1 = str(1,1)
s2 = str([1, 2, 3])

print(f's1:{s1}, type:{type(s1)}')
print(f's2:{s2}, type:{type(s2)}')

print('s1:{},type:{}'.format(s1,type(s1)))
print('s2:{},type:{}'.format(s2,type(s2)))
```
1. 按索引取值
```python
# str 索引取值
msg = 'hello nick'

print(msg[6])
print(f'索引为6: {msg[6]})
print(f'索引为-3: {msg[-3]})
```
2. 切片
```python
# 索引切片
msg = 'hello nick'
#      0123456789 # 索引号

# 前闭后开
print(f'切片1到最后: {msg[1:]}')
print(f'切片1到8: {msg[1:9]}')
print(f'切片1到8，步长为2: {msg[1:9:2]}')

# 步长为正从左到右，步长为负从右到左
print(f'切片所有: {msg[:]}')
print(f'反转所有: {msg[::-1]}')
print(f'切片-5到-2: {msg[-5:-2:1]}')
print(f'切片-2到-5: {msg[-2:-5:-1]}')
```
3. 长度len
``` python
print(len(msg))
```
4. 成员运算in和not in
```python
# str成员运算
msg = 'my name is nick, nick handsome'

print(f"'nick' in msg: {'nick' in msg}")
print(f"'jason' not in msg: {'jason' not in msg}")
```
5. 移除空白strip()
```python
# str移除空白strip()
name = '&&&n ick'
print(f"name.strip('&'): {name.strip('&')}")  # strip()默认为‘ ’，并且不修改原值，新创建空间
print(f"name: {name}")

print(f"'*-& nick+'.strip('*-& +'): {'*-& nick+'.strip('*-& +')}")
```
6. 切分split
```python
# str切分split
info = 'nick:male:19:18:17:16'
info_list1 = info.split(':')
info_list2 = info.split(':', 1) # 切分一次，切分的标志为:
info_list3 = info.split(':', 2) # 切分两次

print(f'info_list1:{info_list1}')
print(f'info_list2:{info_list2}')
print(f'info_list3:{info_list3}')
```
7. 循环
```python
msg = 'hello nick'

for i in msg:
    print(i)
```
8. lstrip()和rstrip()
```python
# str之lstrip()和rstrip()
name = '&&nick&&'

print(f"nick.lstrip('&'): {name.lstrip('&')}")
print(f"nick.rstrip('&'): {name.rstrip('&')}")
```
9. lower()和upper()
```python
# str之lower()和upper()
name = 'Nick Chen'

print(f"name.upper(): {name.lower()}")
print(f"name.upper(): {name.upper()}")
```
10. startswith()和endswith()
```python
# str之startswith()和endswith()
name = 'Nick Chen'

print(f"name.startswith('Nick'): {name.startswith('Nick')}")
print(f"name.endswith('chen'): {name.endswith('chen')}")
print(f"name.endswith('Chen'): {name.endswith('Chen')}")
print(f"name.endswith('ick Chen'): {name.endswith('ick Chen')}")
```
11. rsplit()
```python
# str之rsplit()
info = 'nick:male:19'

print(f"info.rsplit(':', 1): {info.rsplit(':', 1)}")  # 从右开始切分，切分的标志为:
```
12. join()
```python
lis = [1,2,'19']
print(f"':'.join(lis): {':'.join(lis)}")  # 报错，数字不可和字符串拼接

# str之join()
lis = ['nick', 'male', '19']

print(f"':'.join(lis): {':'.join(lis)}") # 拼接处用:连接
print(f"':'.join(lis): {''.join(lis)}") 

```
13. replace()
```python
# str值replace()
name = 'nick shuai'

print(f"name.replace('shuai','handsome'): {name.replace('shuai','handsome')}")
```