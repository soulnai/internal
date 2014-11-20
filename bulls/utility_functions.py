#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import file_utilities
import random

class GameUtilityFunctions(object):



    def __init__(self):
        self.gamefile = "\\\\ws-snastoyaschiy\\Bulls_Cows\\game.txt"
        self.game_number_length = 5
        self.numbers_list = []
        self.try_to_file = 0
        self.bk_get_from_file = [0, 0]
        self.secret_number = 0

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
        list_to_iterate = []
        for num_from_list_to_compare in self.numbers_list:
            bulls = 0
            cows = 0
            num_to_str = str(num_from_list_to_compare)
            for i in range(0, len(my_current_try), 1):
                for j in range(0, len(my_current_try), 1):
                    if num_to_str[i] == my_current_try[j]:
                        if i == j:
                            bulls = bulls + 1
                        else:
                            cows = cows + 1
            if cows != int(self.bk_get_from_file[0]) or bulls != int(self.bk_get_from_file[1]):
                list_to_iterate.append(num_from_list_to_compare)
        if len(list_to_iterate) > 0:
            for elem in list_to_iterate:
                self.numbers_list.remove(elem)

    def generate_secret_number(self):
        self.generate_numbers_list()
        rand_i = random.randint(0, len(self.numbers_list))
        self.secret_number = self.numbers_list[rand_i]
        return self.secret_number

    def return_bulls_cows_to_file(self, try_from_file, secret_number):
        bulls = 0
        cows = 0
        try_num_to_str = str(try_from_file)
        secret_num_to_str = str(secret_number)
        if try_num_to_str.isdigit() and secret_num_to_str.isdigit() and len(try_num_to_str) == self.game_number_length and len(secret_num_to_str):
            for i in range(0, self.game_number_length, 1):
                for j in range(0, self.game_number_length, 1):
                    if try_num_to_str[i] == secret_num_to_str[j]:
                        if i == j:
                            bulls = bulls + 1
                        else:
                            cows = cows + 1
        else:
            print("Some argument is not correct")
        return str(cows) + str(bulls)

    def generate_number(self):
        if len(self.numbers_list) > 1:
            rand_i = random.randint(0, len(self.numbers_list))
            self.try_to_file = self.numbers_list[rand_i]
            return self.try_to_file
        else:
            return self.numbers_list[0]