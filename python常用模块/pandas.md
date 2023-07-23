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

print(df.index)
print(df.columns)
print(df.values)
print(df.T)

# ascending=True表示升序，ascending=False表示降序；inplace=True表示对原始DataFrame本身操作，因此不需要赋值操作，inplace=False相当于是对原始DataFrame的拷贝，之后的一些操作都是针对这个拷贝文件进行操作的，因此需要我们赋值给一个变量，保存操作后的结果。

# 按行标签[c1, c2, c3, c4]从大到小排序
df.sort_index(axis=0)

# 按列标签[2019-01-01, 2019-01-02...]从大到小排序
df.sort_index(axis=1)

# 按c2列的值从大到小排序
df.sort_values(by='c2')

df['c2']
df[['c2', 'c3']]
# 通过自定义的行标签选择数据
print(df.loc['2023-07-31':'2023-09-30'])
```
![Alt text](/assets/10.png)
