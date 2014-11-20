# -*- coding: utf-8 -*-
#stdlib
import sys
import io

#project_classes
import bulls.utility_functions

#testframework
import pytest
import unittest

file = open('parameters.txt', 'r')
file_lines = file.readlines()
file.close()

@pytest.mark.parametrize('param1', file_lines)
@pytest.mark.parametrize('param2', file_lines)
class TestClass(unittest.TestCase):

    def test_bk_output_length(self, param1, param2):
        game = bulls.utility_functions.GameUtilityFunctions()
        func_response = game.return_bulls_cows_to_file(param1, param2)
        assert len(func_response) == 2

    def test_bk_output_is_digit(self, param1, param2):
        game = bulls.utility_functions.GameUtilityFunctions()
        func_response = game.return_bulls_cows_to_file(param1, param2)
        assert func_response.isdigit()