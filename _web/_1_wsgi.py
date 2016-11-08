#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = 'WSGI'
__author__ = 'fangyeqing'
__time__ = '2016/11/4'
"""
from wsgiref.simple_server import make_server


# wsgi标准的http处理函数，包含以下两个输入：
# environ：一个包含所有HTTP请求信息的dict对象；
# start_response：一个发送HTTP响应的函数。
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    # return [b'<h1>Hello, web!</h1>']
    body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]

# 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
httpd = make_server('', 8000, application)
print('Serving HTTP on port 8000...')
# 开始监听HTTP请求:
httpd.serve_forever()


