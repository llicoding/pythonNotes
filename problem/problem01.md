# python代码问题：TypeError: 'list' object is not callable
![Alt text](/assets/02.png)
## error的意思是 list对象不能用函数形式调用，就是不能callable。
简单来说就是list变量和list函数重名了。
检查list变量是否被使用，往前查看，发现第159行定义了一个名为list的变量

![Alt text](/assets/04.png)

检查list的值，发现list已经被占用

![Alt text](/assets/01.png)

删除list变量，确认一下结果，重新调用list()函数

![Alt text](/assets/03.png)

其中range(1, 10)的类型为range