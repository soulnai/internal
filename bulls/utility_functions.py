#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import file_utilities
import random

class GameUtilityFunctions(object):



    def __init__(self):
        self.gamefile = "game.txt"
        self.game_number_length = 5
        self.numbers_list = []
        self.try_to_file = 0
        self.bk_get_from_file = [0, 0]

    def if_number_contain_duplicates(self, number):
        num = str(number)
        for i in range(0, len(num), 1):
            for j in range(0, len(num), 1):
                if num[i] == num[j] and i != j:
                    return False
        return True

    def generate_numbers_list(self):
        for i in range(10 ** (self.game_number_length-1), 10 ** self.game_number_length - 1, 1):
            if self.if_number_contain_duplicates(i):
                self.numbers_list.append(i)

    def analyze_bulls_cows(self):
        my_current_try = str(self.try_to_file)
        for num_from_list_to_compare in self.numbers_list:
            bulls = 0
            cows = 0
            num_to_str = str(num_from_list_to_compare)
            for i in range(0, len(my_current_try), 1):
                for j in range(0, len(my_current_try), 1):
                    if num_to_str[i] == my_current_try[j]:
                        if i == j:
                            bulls = bulls + 1
                        if i != j:
                            cows = cows + 1
            if cows != self.bk_get_from_file[0] or bulls != self.bk_get_from_file[1]:
                self.numbers_list.remove(num_from_list_to_compare)

    def generate_try(self):
        rand_i = random.randint(0, len(self.numbers_list))
        return self.numbers_list[rand_i]


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    file = file_utilities.FileUtilities()


    game = GameUtilityFunctions()
    utils = file_utilities.FileUtilities()
    game.generate_numbers_list()
    utils.write_try_to_file(game.generate_try())
    #print game.numbers_list

    #game.try_to_file = 12345
    #game.bk_get_from_file = file.get_answer(file.read_from_file())
    #print game.bk_get_from_file
    #game.analyze_bulls_cows()
    #print(game.numbers_list)
