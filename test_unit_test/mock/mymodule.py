#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'fangyeqing'
__time__ = '2017/3/8'
"""
import os


def rm(filename):
    os.remove(filename)


def rm_with_if(filename):
    if os.path.isfile(filename):
        os.remove(filename)


class RemovalService(object):
    """A service for removing objects from the filesystem."""

    def rm(filename):
        if os.path.isfile(filename):
            os.remove(filename)


class UploadService(object):
    def __init__(self, removal_service):
        self.removal_service = removal_service

    def upload_complete(self, filename):
        self.removal_service.rm(filename)