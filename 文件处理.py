# 绝对路径
f = open(r'E:/PythonNotes/assets/txt_01.txt', encoding='utf8')
# 相对路径
f = open(r'assets/txt_01.txt', encoding='utf8')

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

print('success')

# rt: read by text
# windows的操作系统默认编码为gbk，因此需要使用utf8编码
f = open('E:/PythonNotes/assets/txt_01.txt', mode='rt', encoding='utf8')
data = f.read()
print(data)
print(f"type(data): {type(data)}")
f.close()

# rb: read by bytes
f = open('E:/PythonNotes/assets/txt_01.txt', mode='rb')
data = f.read()
print(data)
print(f"type(data): {type(data)}")
f.close()

f = open('E:/PythonNotes/assets/txt_01.txt', mode='rt', encoding='utf8')
data1 = f.read()
data2 = f.read()
print(f"data1: {data1}")
print(f"data2: {data2}")
f.close()

# 由于f.read()一次性读取文件的所有内容，如果文件非常大的话，可能会造成内存爆掉，即电脑卡死。因此可以使用f.readline()/f.readlines()读取文件内容。
# f.readline()/f.readlines()
f = open('E:/PythonNotes/assets/txt_01.txt', mode='rt', encoding='utf8')
print(f"f.readable(): {f.readable()}")  # 判断文件是否可读
data1 = f.readline()
# data2 = f.readlines()
print(f"data1: {data1}")
# print(f"data2: {data2}")
f.close()

# wt
f = open('E:/PythonNotes/assets/txt_01.txt', mode='wt', encoding='utf8')
print(f"f.readable(): {f.readable()}")
f.write('nick 真帅呀\n')  # '\n'是换行符
f.write('nick,nick, you drop, I drop.')
f.write('nick 帅的我五体投地')
f.flush()  # 立刻将文件内容从内存刷到硬盘
f.close()

# at
f = open('E:/PythonNotes/assets/txt_01.txt', mode='at', encoding='utf8')
print(f"f.readable(): {f.readable()}")
f.write('nick 真帅呀\n')  # '\n'是换行符
f.write('nick,nick, you drop, I drop.')
f.write('nick 帅的我五体投地')
f.close()

import os

with open('E:/PythonNotes/assets/txt_02.txt') as fr,\
    open('E:/PythonNotes/assets/txt_03.txt','w') as fw:
    data = fr.read() # 全部读入内存,如果文件很大,会很卡
    data = data.replace('nick','nicknb') # 在内存中完成修改

    fw.write(data)  # 新文件一次性写入原文件内容

# 删除原文件
os.remove('E:/PythonNotes/assets/txt_02.txt')
# 重命名新文件名为原文件名
os.rename('E:/PythonNotes/assets/txt_03.txt','E:/PythonNotes/assets/txt_02.txt')