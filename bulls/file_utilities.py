#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import utility_functions


class FileUtilities(object):

    def read_from_file(self):
        utility_instance = utility_functions.GameUtilityFunctions()
        file = open(utility_instance.gamefile, 'r')
        file_lines = file.readlines()
        file.close()
        return file_lines

    def get_answer(self, lines_from_file):
        answer = lines_from_file[-1]
        if len(answer) != 3:
            if len(lines_from_file) > 1:
                answer = lines_from_file[-2]
                if len(answer) == 3:
                    answer_arr = [answer[0], answer[1]]
                    print "cows", answer_arr[0]
                    print "bulls", answer_arr[1]
                    return answer_arr
                else:
                    print ("Something goes wrong")
            else:
                print ("Something goes wrong")
        else:
            if len(answer) == 3:
                answer_arr = [answer[0], answer[1]]
                print "cows", answer_arr[0]
                print "bulls", answer_arr[1]
                return answer_arr
        #print ("Something goes wrong")

    def write_try_to_file(self, try_number):
        game = utility_functions.GameUtilityFunctions()
        file = open(game.gamefile, 'a+')
        file.write(str(try_number)+"\n")
        file.close()

#game = utility_functions.GameUtilityFunctions()
#print game.generate_numbers_list()
#print game.numbers_list
#try_num = game.generate_try()
#print try_num
#inst = FileUtilities()
#inst.get_answer(inst.read_from_file())