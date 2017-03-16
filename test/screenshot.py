#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'fangyeqing'
__time__ = '2017/3/16'
"""
import time
from PIL import Image
from selenium import webdriver


class ScreenShort(object):
    def __init__(self):
        self.driver = webdriver.PhantomJS(executable_path='phantomjs.exe')

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.driver.quit()

    def get(self, url, time_out=300, windows_size=(1280, 800)):
        driver = self.driver
        driver.set_page_load_timeout(time_out)
        driver.set_window_size(windows_size[0], windows_size[1])
        driver.get(url)

    def get_screen_short(self, save_path=None):
        if not save_path:
            save_path = 'screenshot'+ time.strftime('-%Y-%m-%d %H-%I-%M-%S', time.localtime(time.time()))+'.png'
        self.driver.get_screenshot_as_file(save_path)

    def get_element_by_id(self, element_id, save_path=None):
        if not save_path:
            save_path = 'get_element'+ time.strftime('-%Y-%m-%d %H-%I-%M-%S', time.localtime(time.time()))+'.png'
        imgelement = self.driver.find_element_by_id(element_id)
        location = imgelement.location
        size = imgelement.size
        self.driver.save_screenshot(save_path)
        im = Image.open(save_path)
        left = location['x']
        top = location['y']
        right = left + size['width']
        bottom = location['y'] + size['height']
        im = im.crop((left, top, right, bottom))
        im.save(save_path)

if __name__ == '__main__':
    with ScreenShort() as ss:
        url = 'https://www.baidu.com/'
        save_path = r'get-id-lg.png'
        ss.get(url)
        ss.get_screen_short()
        ss.get_element_by_id(element_id='lg', save_path=save_path)