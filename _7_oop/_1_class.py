#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = '类和实例'
__author__ = 'fangyeqing'
__time__ = '2016/11/3'
"""
from types import MethodType


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

# 对象动态添加属性
bart = Student('Bart Simpson', 59)
bart.age = 8
bart.print_score()
print(bart.age)


# 对象动态添加方法
def set_age(self, age):
    self.age = age
lisa = Student('Lisa Simpson', 87)
lisa.set_age = MethodType(set_age, lisa)
lisa.set_age(8)
print(lisa.age)


# 给类定义方法
def set_score(self, score):
    self.score = score
Student.set_score = set_score
lisa.set_score(10)
bart.set_score(10)
print(lisa.score)
