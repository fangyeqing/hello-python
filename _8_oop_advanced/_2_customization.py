#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'fangyeqing'
__time__ = '2016/11/3'
"""


# __str__：重写toString
# __getattr__:可以用于防止没有此属性
# __call__:相当于对象.method()，省略掉方法，默认调用__call__
class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name

    def __getattr__(self, attr):
        if attr == 'score':
            return 99
        elif attr == 'age':
            return lambda: 25
        else:
            raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)

    def __call__(self):
        print('My name is %s.' % self.name)
stu = Student('Michael')
print(stu)
print(stu.score)
print(stu.age)
# print(stu.phone)
print(stu())
callable(stu)


# __getattr__应用:链式调用
class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path
print(Chain().status.user.timeline.list)


# __iter__和__next__:将斐波那契数列改成可以for循环的形式
# __getitem__:使其实现取元素的功能
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100: # 退出循环的条件
            raise StopIteration();
        return self.a # 返回下一个值

    def __getitem__(self, n):
        if isinstance(n, int):  # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):  # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L
for n in Fib():
    print(n)
f = Fib()
print(f[3])
print(f[:5])
