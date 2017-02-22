#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = 'web框架'
__author__ = 'fangyeqing'
__time__ = '2016/11/4'
"""


from flask import Flask
from flask import request

app = Flask(__name__)


# 主页面
@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Home</h1>'


# 登录页面，GET请求
@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''


# 登录页面，Post请求，处理登录请求
@app.route('/signin', methods=['POST'])
def signin():
    # 需要从request对象读取表单内容：
    if request.form['username'] == 'admin' and request.form['password'] == 'password':
        return '<h3>Hello, admin!</h3>'
    return '<h3>Bad username or password.</h3>'

if __name__ == '__main__':
    app.run()
