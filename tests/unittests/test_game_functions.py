from __future__ import unicode_literals
# -*- coding: utf-8 -*-


import unittest
from unittest import TestCase
import game.game_logic_functions

__author__ = 'avasilyev2'


class TestGameUtilityFunctions(TestCase):

    def test_all_digits_are_unique_return_type(self):

        #given
        file = open('parameters.txt', 'r')
        file_lines = file.readlines()
        file.close()
        params_to_check = file_lines
        #execute
        for i in params_to_check:
            response = game.game_logic_functions.all_digits_are_unique(i)
            #result
            assert type(response) == bool

    def test_generate_numbers_list_returns_non_empty(self):
        #given
        params_to_check = [1, 2, 5]
        #execute
        for i in params_to_check:
            response = game.game_logic_functions.generate_numbers_list(i)
            #result
            assert len(response) > 0

        pass

    def test_analyze_bulls_cows_and_remove_number_list(self):
        #given
        numbers_list = [12345, 12346, 11235, 12347]
        bk_stub = "05"
        number_stub = 12347
        #execute
        func_response = game.game_logic_functions.analyze_bulls_cows_and_remove_number_list(bk_stub, number_stub, numbers_list)
        #result
        self.assertNotEqual(len(func_response), 0, "Number list should consist of more than 0 elements")

    def test_generate_secret_number(self):
        #given
        numbers_list = [12345, 12346, 11235, 12347]
        #execute
        func_response = game.game_logic_functions.generate_secret_number(numbers_list)
        #result
        self.assertIsNotNone(func_response, 'Return should be non empty')

    def test_return_bulls_cows_to_file(self):
        #given
        try_from_file = 12345
        secret_number = 12346
        #execute
        func_response = game.game_logic_functions.return_bulls_cows_to_file(try_from_file, secret_number)
        self.assertEqual(func_response, "04", "Response should be = 04")

    def test_generate_number(self):
        #given
        numbers_list = [12345, 12346, 11235, 12347]
        #execute
        func_response = game.game_logic_functions.generate_number(numbers_list)
        #result
        self.assertIsNotNone(func_response, 'Return should be non empty')
        pass

if __name__ == '__main__':
    unittest.main()