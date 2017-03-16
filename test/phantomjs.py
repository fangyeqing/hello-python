#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'fangyeqing'
__time__ = '2017/3/16'
"""
from PIL import Image
from selenium import webdriver


def webscreen():
    url = 'https://www.baidu.com/'
    driver = webdriver.PhantomJS(executable_path='phantomjs.exe')
    driver.set_page_load_timeout(300)
    driver.set_window_size(1280, 800)
    driver.get(url)
    driver.get_screenshot_as_file('screenshot.png')
    imgelement = driver.find_element_by_id('lg')
    location = imgelement.location
    size = imgelement.size
    savepath = r'get-id-lg.png'
    driver.save_screenshot(savepath)
    im = Image.open(savepath)
    left = location['x']
    top = location['y']
    right = left + size['width']
    bottom = location['y'] + size['height']
    im = im.crop((left, top, right, bottom))
    im.save(savepath)

webscreen()