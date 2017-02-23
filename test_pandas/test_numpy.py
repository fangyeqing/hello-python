#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'fangyeqing'
__time__ = '2017/2/22'
"""

import numpy as np
import time
import math


a = np.array([1, 2, 3, 4])
b = np.array((1, 2, 3, 4), dtype=np.float)
c = np.array([[1, 2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 10]])
print(a, '\n', b, '\n', c)
print(a.dtype, b.dtype, a.shape, c.shape)

c.shape = 4, 3
print(c)
c.shape = 2, -1
print(c)
d = a.reshape((2, 2))
print(d)
print(a)
a[1] = 100  # 将数组a的第一个元素改为100
print(d)    # 注意数组d中的2也被改变了


print(np.arange(0, 1, 0.1))
print(np.linspace(0, 1, 12))
print(np.logspace(0, 2, 20))

s = "abcdefgh"
print(np.fromstring(s, dtype=np.int8))
print(np.fromstring(s, dtype=np.int16))


# 构造一维数组，a(i)=i%4+1
def func(i):
    return i % 4 + 1
print(np.fromfunction(func, (10,)))


# 构造二位数组，a（i,j）=(i+1)*(j+1)
def func2(i, j):
    return (i+1) * (j+1)
print(np.fromfunction(func2, (9, 9)))


a = np.arange(10)
print(a[5])    # 用整数作为下标可以获取数组中的某个元素
print(a[3:5])  # 用范围作为下标获取数组的一个切片，包括a[3]不包括a[5]
print(a[:5])   # 省略开始下标，表示从a[0]开始
print(a[:-1])  # 下标可以使用负数，表示从数组后往前数
a[2:4] = 100, 101    # 下标还可以用来修改元素的值
print(a)
print(a[1:-1:2])   # 范围中的第三个参数表示步长，2表示隔一个元素取一个元素
print(a[::-1])  # 省略范围的开始下标和结束下标，步长为-1，整个数组头尾颠倒
print(a[5:1:-2])  # 步长为负数时，开始下标必须大于结束下标


b = a[3:7]  # 通过下标范围产生一个新的数组b，b和a共享同一块数据空间
print(b)
b[2] = -10  # 将b的第2个元素修改为-10
print(a)  # a的第5个元素也被修改为10


x = np.arange(10, 1, -1)
print(x)
print(x[[3, 3, 1, 8]])  # 获取x中的下标为3, 3, 1, 8的4个元素，组成一个新的数组
b = x[np.array([3, 3, -3, 8])]  # 下标可以是负数
b[2] = 100
print(x)  # 由于b和x不共享数据空间，因此x中的值并没有改变
x[[3, 5, 1]] = -1, -2, -3  # 整数序列下标也可以用来修改元素的值
print(x)


x = np.arange(5, 0, -1)
print(x)
print(x[np.array([True, False, True, False, False])])  # 布尔数组中下标为0，2的元素为True，因此获取x中下标为0,2的元素
print(x[[True, False, True, False, False]])  # 如果是布尔列表，则把True当作1, False当作0，按照整数序列方式获取x中的元素
print(x[np.array([True, False, True, True])])  # 布尔数组的长度不够时，不够的部分都当作False
x[np.array([True, False, True, True])] = -1, -2, -3  # 布尔数组下标也可以用来修改元素
print(x)


x = np.random.rand(10) # 产生一个长度为10，元素值为0-1的随机数的数组
print(x[x > 0.5])


a = np.arange(0, 60, 10).reshape(-1, 1) + np.arange(0, 6)
print(a)
print(a[0, 3:5])
print(a[4:, 4:])
print(a[:, 2])
print(a[2::2, ::2])
print(a[(0, 1, 2, 3, 4), (1, 2, 3, 4, 5)])
print(a[3:, [0, 2, 5]])
mask = np.array([1, 0, 1, 0, 0, 1], dtype=np.bool)
print(a[mask, 2])


persontype = np.dtype({
    'names': ['name', 'age', 'weight'],
    'formats': ['S32', 'i', 'f']})
a = np.array([("Zhang", 32, 75.5), ("Wang", 24, 65.2)], dtype=persontype)
print(a.dtype)
print(a)
print(a[0])
c = a[1]
c["name"] = "Li"
print(a[1]["name"])
b = a[:]["age"]
print(b)
b[0] = 40
print(a[0]["age"])


a = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]], dtype=np.float32)
print(a.dtype)
print(a.ndim)
print(a.shape)
print(a.strides)
print(a.data)
b = a[::2, ::2]
print(b)
print(b.strides)

c = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]], dtype=np.float32, order="F")
print(c.strides)


x = np.linspace(0, 2*np.pi, 10)
y = np.sin(x)
print(y)
t = np.sin(x, x)
print(id(t) == id(x))

'''
x = [i * 0.001 for i in range(1000000)]
start = time.clock()
for i, t in enumerate(x):
    x[i] = math.sin(t)
print("math.sin:", time.clock() - start)

x = [i * 0.001 for i in range(1000000)]
x = np.array(x)
start = time.clock()
np.sin(x, x)
print("numpy.sin:", time.clock() - start)

x = [i * 0.001 for i in range(1000000)]
start = time.clock()
for i, t in enumerate(x):
    x[i] = np.sin(t)
print("numpy.sin loop:", time.clock() - start)
'''
# 输出
# math.sin: 0.41831748538827573
# numpy.sin: 0.011924890681391243
# numpy.sin loop: 1.4091675317012233


a = np.arange(0, 4)
b = np.arange(1, 5)
print(a)
print(b)
print(np.add(a, b))
print(a + b)
print(np.add(a, b, a))
print(a)

'''
a = np.arange(0, 100000000)
b = np.arange(0, 100000000)
start = time.clock()
x = a*b + a
print("x = a*b+c time:", time.clock() - start)
start = time.clock()
y = a*b
y += a
print("y = a*b,y += c time:", time.clock() - start)
'''


def triangle_wave(x, c, c0, hc):
    x = x - int(x)   # 三角波的周期为1，因此只取x坐标的小数部分进行计算
    if x >= c: r = 0.0
    elif x < c0: r = x / c0 * hc
    else: r = (c-x) / (c-c0) * hc
    return r
x = np.linspace(0, 2, 1000)
y = np.array([triangle_wave(t, 0.6, 0.4, 1.0) for t in x])

triangle_ufunc = np.frompyfunc( lambda x: triangle_wave(x, 0.6, 0.4, 1.0), 1, 1)
y2 = triangle_ufunc(x)


def triangle_func(c, c0, hc):
    def trifunc(x):
        x = x - int(x) # 三角波的周期为1，因此只取x坐标的小数部分进行计算
        if x >= c: r = 0.0
        elif x < c0: r = x / c0 * hc
        else: r = (c-x) / (c-c0) * hc
        return r
    # 用trifunc函数创建一个ufunc函数，可以直接对数组进行计算, 不过通过此函数
    # 计算得到的是一个Object数组，需要进行类型转换
    return np.frompyfunc(trifunc, 1, 1)
y2 = triangle_func(0.6, 0.4, 1.0)(x)


# 广播
a = np.arange(0, 60, 10).reshape(-1, 1)    # [[ 0], [10], [20], [30], [40], [50]]
b = np.arange(0, 5)    # [0 1 2 3 4]
print(a, '\n', b)
print(a.shape, b.shape)    # 输出：(6, 1) (5,)
print(a + b)

b.shape = 1, 5
print(b)
b = b.repeat(6, axis=0)
a = a.repeat(5, axis=1)
print(a, b, sep='\n')
print(a + b)

x, y = np.ogrid[0:1:4j, 0:1:3j]
print(x, y)

a = np.add.reduce([1, 2, 3])  # 1 + 2 + 3
b = np.add.reduce([[1, 2, 3], [4, 5, 6]], axis=0)  # 1+2+3 , 4+5+6
c = np.add.reduce([[1, 2, 3], [4, 5, 6]], axis=1)  # 1+4 , 2+5 ,3+6
print(a, b, c, sep='\n')


a = np.add.accumulate([1, 2, 3])  # [1 3 6]
b = np.add.accumulate([[1, 2, 3], [4, 5, 6]], axis=0)  # [[1 2 3],[5 7 9]]
c = np.add.accumulate([[1, 2, 3], [4, 5, 6]], axis=1)  # [[ 1  3  6],[ 4  9 15]]
print(a, b, c, sep='\n')


a = np.array([1, 2, 3, 4])
result = np.add.reduceat(a, indices=[0, 1, 0, 2, 0, 3, 0])
print(result)


x = np.multiply.outer([1, 2, 3, 4, 5], [2, 3, 4])
print(x)   # [[ 2  3  4],[ 4  6  8],[ 6  9 12],[ 8 12 16],[10 15 20]]


a = np.matrix([[1, 2, 3], [5, 5, 6], [7, 9, 9]])
print(a*a**-1)


a = np.arange(0, 12)
a.shape = 3, 4
print(a)
a.tofile("a.bin")
b = np.fromfile("a.bin", dtype=np.float)  # 按照float类型读入数据
print(b)  # 读入的数据是错误的
b = np.fromfile("a.bin", dtype=np.int32)  # 按照int32类型读入数据
print(b)  # 数据是一维的
b.shape = 3, 4  # 按照a的shape修改b的shape
print(b)  # 这次终于正确了


np.save("a.npy", a)
c = np.load("a.npy")
print(c)


a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.arange(0, 1.0, 0.1)
c = np.sin(b)
np.savez("result.npz", a, b, sin_array=c)
r = np.load("result.npz")
print(r["arr_0"])  # 数组a
print(r["arr_1"])  # 数组b
print(r["sin_array"])  # 数组c


a = np.arange(0, 12, 0.5).reshape(4, -1)
np.savetxt("a.txt", a)  # 缺省按照'%.18e'格式保存数据，以空格分隔
b = np.loadtxt("a.txt")
np.savetxt("a.txt", a, fmt="%d", delimiter=",")  # 改为保存为整数，以逗号分隔
c = np.loadtxt("a.txt", delimiter=",")  # 读入的时候也需要指定逗号分隔
print(a, b, c, sep='\n')

