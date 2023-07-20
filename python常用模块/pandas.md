# Series数据结构
Series是一种类似于一维数组的对象，由一组数据和一组与之相关的数据标签（索引）组成。
Series比较像列表（数组）和字典的结合体
```python
import numpy as np
import pandas as pd

df = pd.Series(0, index = ['a', 'b', 'c', 'd'])
print(df)

print(df.values)

arr = np.array([1, 2, 3, 4, np.nan])
print(arr)

df = pd.Series(arr, index = ['a', 'b', 'c', 'd', 'e'])
print(df)

print(df**2)

print(df[0])
print(df['a'])
print(df[[0, 1, 2]])
print(df[0:2])
np.sin(df)
print(df[df >  1])
```
# DataFrame数据结构
DataFrame是一个表格型的数据结构，含有一组有序的列。
DataFrame可以被看做是由Series组成的字典，并且共用一个索引。
```python
dates = pd.date_range('20230720', periods=6, freq='M')
print(dates)

np.random.seed(1)
arr = 10 * np.random.randn(6, 4)
print(arr)

df = pd.DataFrame(arr, index=dates, columns=['c1', 'c2', 'c3', 'c4'])
```
