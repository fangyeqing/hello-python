#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'root'
__time__ = '2/16/17'
"""
import functools


def log1(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


def log2(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


def log3(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


def log4(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@log1
def now1():
    print('2015-3-25')


@log2('execute')
def now2():
    print('2015-3-25')


@log3
def now3():
    print('2015-3-25')


@log4('execute')
def now4():
    print('2015-3-25')


now1()
print('now1.__name__:%s' % now1.__name__)
now2()
print('now2.__name__:%s' % now2.__name__)
now3()
print('now3.__name__:%s' % now3.__name__)
now4()
print('now4.__name__:%s' % now4.__name__)


# 请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志。
def log(func):
    def wrapper():
        print('begin call')
        func()
        print('end call')
    return wrapper


@log
def now():
    print('2017-2-14')
now()


# 再思考一下能否写出一个@log的decorator，使它既支持
def log(args):
    if isinstance(args, str):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print('begin %s %s():'%(args,func.__name__))
                func(*args, **kw)
                print('end %s %s():'%(args,func.__name__))
            return wrapper
        return decorator
    else:
        func = args
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('begin call %s():' % func.__name__)
            func(*args, **kw)
            print('end call %s():'%func.__name__)
        return wrapper


@log
def now():
    print('2015-3-25')
now()


@log('exective')
def tomorrow():
    print('2017/2/13')

now()
tomorrow()