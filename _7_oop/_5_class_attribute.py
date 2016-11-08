#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = '实例属性和类属性'
__author__ = 'fangyeqing'
__time__ = '2016/11/3'
"""


# 学生
class Student(object):
    # 用于记录已经注册学生数
    student_number = 0

    def __init__(self, name):
        self.name = name


# 注册一个学生:注册必填项名字，选填项利用关键字参数传递。注册完成，学生数+1
def register(name, **kw):
    a = Student(name)
    for k, v in kw.items():
        setattr(a, k, v)
    Student.student_number += 1
    return a
bob = register('Bob', score=90)
ah = register('Ah', age=8)

print(getattr(bob, 'score'))
print(getattr(ah, 'age'))
print(Student.student_number)
