# 用python实现loading动态等待功能
在python中，print()函数自带换行符
## print()函数中有一个内置函数"end",使用print()时默认end="\n"

为了实现loading不换行需求，可把end设置为""（空字符）即可实现

``` python
import time

print("loading",end = '')
for i in range(6):
    print(".", end = '')
    time.sleep(0.2)
```