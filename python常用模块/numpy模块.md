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