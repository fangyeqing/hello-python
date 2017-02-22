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
    response_body = [
        '%s: %s' % (key, value) for key, value in sorted(environ.items())
    ]
    response_body = '\n'.join(response_body)  # 由于下面将Content-Type设置为text/plain，所以`\n`在浏览器中会起到换行的作用
    status = '200 OK'
    response_headers = [
        ('Content-Type', 'text/plain'),
        ('Content-Length', str(len(response_body)))
    ]
    start_response(status, response_headers)
    return [response_body]


# 中间件
class Upperware:
   def __init__(self, app):
      self.wrapped_app = app

   def __call__(self, environ, start_response):
      for data in self.wrapped_app(environ, start_response):
        yield data.upper()

# 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
#httpd = make_server('', 8000, application)
wrapped_app = Upperware(application)
httpd = make_server('', 8000, wrapped_app)
print('Serving HTTP on port 8000...')
# 开始监听HTTP请求:
httpd.serve_forever()


