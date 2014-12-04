from __future__ import unicode_literals
#! /usr/bin/env python
# -*- coding: utf-8 -*-


import unittest
from unittest import TestCase
import game.utility_functions

__author__ = 'avasilyev2'


class TestGameUtilityFunctions(TestCase):

    def test_if_number_contain_duplicates_return_type(self):

        #given
        file = open('parameters.txt', 'r')
        file_lines = file.readlines()
        file.close()
        params_to_check = file_lines
        #execure
        for i in params_to_check:
            response = game.utility_functions.GameUtilityFunctions.if_number_contain_duplicates(i)
            #result
            assert type(response) == bool

    def test_generate_numbers_list_returns_non_empty(self):
        #given
        params_to_check = [0, 1, 2, 5]
        #execure
        for i in params_to_check:
            response = game.utility_functions.GameUtilityFunctions.generate_numbers_list(i)
            #result
            assert len(response) > 0

        pass

    def test_analyze_bulls_cows_and_remove_number_list(self):
        pass

    def test_generate_secret_number(self):
        pass

    def test_return_bulls_cows_to_file(self):
        pass

    def test_generate_number(self):
        pass

if __name__ == '__main__':
    unittest.main()