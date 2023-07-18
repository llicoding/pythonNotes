# 绝对路径
f = open(r'E:/PythonNotes/assets/txt_01.txt')
# f = open('E:\\PythonNotes\\assets\\txt_01.txt')

data_01 = f.read()
# data_02 = f.readline()

print(data_01)
# print(data_02)

# 由于Python的垃圾回收机制只回收引用计数为0的变量，但是打开文件还占用操作系统的资源，所以我们需要回收操作系统的资源资源
f.close()

# write模式打开文件
f = open(r'E:/PythonNotes/assets/txt_01.txt', mode='w')
f.write("""name = 'nick'
        pwd = '1234'""")
f.close()
f = open(r'E:/PythonNotes/assets/txt_01.txt', mode='r')
data = f.read()
print(data)
