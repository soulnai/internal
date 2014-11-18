#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import utility_functions

class FileUtilities(object):

    def read_from_file(self):
        utility_instance = utility_functions.GameUtilityFunctions()
        #print utility_instance.gamefile
        file = open(utility_instance.gamefile, 'r')
        #print utility_instance.gamefile
        file_lines = file.readlines()
        #print file_lines[-1]
        return file_lines

    def get_answer(self, lines_from_file):
        answer = lines_from_file[-1]
        answer_arr = [answer[0], answer[1]]
        print "cows", answer_arr[0]
        print "bulls", answer_arr[1]
        return answer_arr

    def write_try_to_file(self, try_number):
        game = utility_functions.GameUtilityFunctions()
        file = open(game.gamefile, 'a+')
        file.write(str(try_number)+"\n")

#game = utility_functions.GameUtilityFunctions()
#print game.generate_numbers_list()
#print game.numbers_list
#try_num = game.generate_try()
#print try_num
#inst = FileUtilities()
#inst.get_answer(inst.read_from_file())