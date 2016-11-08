#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'fangyeqing'
__time__ = '2016/11/3'
"""


# 父类-动物
class Animal(object):
    def run(self):
        print('Animal is running...')


# 父类-尖叫
class MixlnBark(object):
    def bark(self):
        print("Barking....");


# 方法：依赖于run方法
def run_twice(animal):
    animal.run()
    animal.run()


# 多重继承示例
class Dog(Animal,MixlnBark):
    def run(self):
        print("Dog is Running");

dog = Dog();
dog.run()
dog.bark()


# 动态语言示例
class Timer(object):
    def run(self):
        print('Start...')
run_twice(Dog())
run_twice(Timer())




