#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import file_utilities
import utility_functions
import time


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    game_play = True
    game = utility_functions.GameUtilityFunctions()
    utils = file_utilities.FileUtilities()
    game.generate_numbers_list()
    tries_count = 0
    while game_play:
        if len(game.numbers_list) > 0:
            lines = utils.read_from_file()
            if len(lines[-1])<=3:
                utils.write_try_to_file(game.generate_number())
                game.bk_get_from_file = utils.get_answer(utils.read_from_file())
                if game.bk_get_from_file != None:
                    time.sleep(1)
                    game.analyze_bulls_cows()
                    if game.bk_get_from_file[0] == 0 and game.bk_get_from_file[1] == 5:
                        print "Win"
                        game_play = False
                        break
        tries_count += 1
        time.sleep(1)
        if tries_count > 1000:
            print "Something wrong"
            game_play = False
            break



    #utils.write_try_to_file(game.generate_number())
        utils.get_answer(utils.read_from_file())