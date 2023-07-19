# 创建numpy数组
numpy数组即numpy的ndarray对象，创建numpy数组就是把一个列表传入np.array()方法
```python
import numpy as np

# 创建一维的ndarray对象
arr = np.array([1, 2, 3])
print(arr, type(arr))

# 创建二维的ndarray对象
print(np.array([[1, 2, 3], [4, 5, 6]]))

# 数组的形状用shape，以元组表示
print(np.array([[1, 2, 3], [4, 5, 6]]).shape)
```
# numpy数组的常用属性
![Alt text](/assets/07.png)
```python
arr = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.float32)
print(arr)
print(arr.T)

print(arr.size)

print(arr.ndim)

print(arr.shape)
```
# 获取numpy数组的行列数
由于numpy数组是多维的，对于二维的数组而言，numpy数组就是既有行又有列
```python
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)

# 获取numpy数组的行和列构成的数组
print(arr.shape)

# 获取numpy数组的行
print(arr.shape[0])

# 获取numpy数组的列
print(arr.shape[1])
```
# 切割numpy数组
切分numpy数组类似于列表的切割，但是与列表的切割不同的是，numpy数组的切割涉及到行和列的切割，但是两者切割的方式都是从索引0开始，并且取头不取尾。
```python
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(arr)

# 取所有元素
print(arr[:, :])

# 取第一行的所有元素
print(arr[:1, :])

# 取第一行的所有元素
print(arr[0, [0, 1, 2, 3]])

# 取第一列的所有元素
print(arr[:, :1])

# 取第一列的所有元素
print(arr[(0, 1, 2), 0])

# 取第一行第一列的元素
print(arr[0, 0])

# 取大于5的元素，返回一个数组
print(arr[arr > 5])

# numpy数组按运算符取元素的原理，即通过arr > 5生成一个布尔numpy数组
print(arr > 5)
```
# numpy数组元素替换
numpy数组元素的替换，类似于列表元素的替换，并且numpy数组也是一个可变类型的数据，即如果对numpy数组进行替换操作，会修改原numpy数组的元素，所以下面我们用.copy()方法举例numpy数组元素的替换。
```python
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(arr)

# 取第一行的所有元素，并且让第一行的元素都为0
arr1 = arr.copy()
arr1[:1, :] = 0
print(arr1)

# 取所有大于5的元素，并且让大于5的元素为0
arr2 = arr.copy()
arr2[arr > 5] = 0
print(arr2)

# 对numpy数组清零
arr3 = arr.copy()
arr3[:, :] = 0
print(arr3)
```
# numpy数组的合并
```python
arr1 = np.array([[1, 2], [3, 4], [5, 6]])
print(arr1)
arr2 = np.array([[7, 8], [9, 10], [11, 12]])
print(arr2)

# 合并两个numpy数组的行，注意使用hstack()方法合并numpy数组，numpy数组应该有相同的行，其中hstack的h表示horizontal水平的
print(np.hstack((arr1, arr2)))

# 合并两个numpy数组的列，注意使用vstack()方法合并numpy数组，numpy数组应该有相同的列，其中vstack的v表示vertical垂直的
print(np.vstack((arr1, arr2)))

# 合并两个numpy数组，其中axis=0表示合并两个numpy数组的列
print(np.concatenate((arr1, arr2), axis=0))
```
![Alt text](/assets/08.png)
1. array()
```python
arr = np.array([1, 2, 3])
print(arr)
```
2. arange()
```python
# 构造0-9的ndarray数组
print(np.arange(10))
```
```python
# 构造1-4的ndarray数组
print(np.arange(1, 5))
```
```python
# 构造1-19且步长为2的ndarray数组
print(1, 20, 2)
```
3. zeros()/ones()/eye()/empty()
```python
# 构造3*4的全为0的numpy数组
print(np.zeros((3, 4)))
```
```python
# 构造3*4的全为1的numpy数组
print(np.ones((3, 4)))
```