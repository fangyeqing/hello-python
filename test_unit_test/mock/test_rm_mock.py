#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'fangyeqing'
__time__ = '2017/3/8'
"""
import unittest

import mock

from test_unit_test.mock.mymodule import rm,rm_with_if, RemovalService, UploadService


class RmTestCase(unittest.TestCase):
    @mock.patch('test_unit_test.mock.mymodule.os')
    def test_rm(self, mock_os):
        rm("any path")
        # test that rm called os.remove with the right parameters
        mock_os.remove.assert_called_with("any path")

    @mock.patch('test_unit_test.mock.mymodule.os.path')
    @mock.patch('test_unit_test.mock.mymodule.os')
    def test_rm_with_if(self, mock_os, mock_path):
        # set up the mock
        mock_path.isfile.return_value = False
        rm_with_if("any path")
        # test that the remove call was NOT called.
        self.assertFalse(mock_os.remove.called, "Failed to not remove the file if not present.")
        # make the file 'exist'
        mock_path.isfile.return_value = True
        rm_with_if("any path")
        mock_os.remove.assert_called_with("any path")


class RemovalServiceTestCase(unittest.TestCase):
    @mock.patch('test_unit_test.mock.mymodule.os.path')
    @mock.patch('test_unit_test.mock.mymodule.os')
    def test_rm(self, mock_os, mock_path):
        # instantiate our service
        reference = RemovalService()
        # set up the mock
        mock_path.isfile.return_value = False
        reference.rm("any path")
        # test that the remove call was NOT called.
        self.assertFalse(mock_os.remove.called, "Failed to not remove the file if not present.")
        # make the file 'exist'
        mock_path.isfile.return_value = True
        reference.rm("any path")
        mock_os.remove.assert_called_with("any path")


class UploadServiceTestCase(unittest.TestCase):
    @mock.patch.object(RemovalService, 'rm')
    def test_upload_complete(self, mock_rm):
        # build our dependencies
        removal_service = RemovalService()
        reference = UploadService(removal_service)
        # call upload_complete, which should, in turn, call `rm`:
        reference.upload_complete("my uploaded file")
        # check that it called the rm method of any RemovalService
        mock_rm.assert_called_with("my uploaded file")
        # check that it called the rm method of _our_ removal_service
        removal_service.rm.assert_called_with("my uploaded file")


class UploadServiceTestCase2(unittest.TestCase):
    @mock.patch.object(RemovalService, 'rm')
    def test_upload_complete(self, mock_rm):
        # build our dependencies
        mock_removal_service = mock.create_autospec(RemovalService)
        reference = UploadService(mock_removal_service)
        # call upload_complete, which should, in turn, call `rm`:
        reference.upload_complete("my uploaded file")
        # test that it called the rm method
        mock_removal_service.rm.assert_called_with("my uploaded file")