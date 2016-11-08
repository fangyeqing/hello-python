#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'fangyeqing'
__time__ = '2016/11/7'
"""

# list
classmates = ['Michael', 'Bob', 'Tracy']    #list初始化
print(classmates)
print(len(classmates))                        #list长度len()
print(classmates[0])                             #取序号处元素
print(classmates[-1])                      #反向取序号处元素

classmates.append('Adam')       #末尾插入
print(classmates)
classmates.insert(1, 'Jack')    #序号处插入
print(classmates)
classmates.pop()                #删除末尾
print(classmates)
classmates.pop(1)               #删除序号处
print(classmates)
classmates[1] = 'Sarah'         #序号处替换
print(classmates)

L = ['Apple', 123, True]
print(L)

s = ['python', 'java', ['asp', 'php'], 'scheme']
print(s[2])

L = []
print(len(L))

# tuple
classmates = ('Michael', 'Bob', 'Tracy')
print(classmates)
t = (1,)
print(t)

t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)

# map
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}     #初始化
print(d['Michael'])                             #取key为xxx的值，key不存在会报错
d['Adam'] = 67                                  #给key给xxx的赋值
print('Thomas' in d)                            #判断key是否存在
print(d.get('Thomas'))                          #取key为xxx的值，不存在返回空
print(d.get('Thomas', -1))                      #取key为xxx的值，不存在返回-1
print(d.pop('Bob'))                             #删除key为xxx

# set
s = set([1, 2, 3])
print(s)

s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2)
print(s1 | s2)