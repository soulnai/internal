#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#stdlib
import sys

#project_classes
import bulls.utility_functions

#testframework
import pytest
import unittest

class CheckBkFunctionReturnCorrectData(unittest.TestCase):

    def setUp(self):
        """Read test data from file"""


    def tearDown(self):
        a=1

    def test_bk_output(self):
        game = bulls.utility_functions.GameUtilityFunctions()
        func_response = game.return_bulls_cows_to_file(12345, 12345)
        self.assertEqual(len(func_response), 2, 'incorrect return size')

if __name__ == "__main__":
    #sys.argv = ['', 'Test.testName']
    pytest.main()