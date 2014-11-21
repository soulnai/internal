#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import file_utilities
import utility_functions
import time
import sys
import io


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    game_mode = raw_input()
    if game_mode == "client":
        game_play = True
        game = utility_functions.GameUtilityFunctions()
        utils = file_utilities.FileUtilities()
        game.generate_numbers_list()
        tries_count = 0
        utils.write_try_to_file(game.generate_number())
        while game_play:
            if len(game.numbers_list) > 0:
                lines = utils.read_from_file()
                game.bk_get_from_file = utils.get_answer(lines)
                if game.bk_get_from_file != None:
                    game.analyze_bulls_cows()
                    print len(game.numbers_list)
                    if int(game.bk_get_from_file[0]) == 0 and int(game.bk_get_from_file[1]) == 5:
                        print "Win"
                        game_play = False
                        sys.exit(0)
                        break
                    utils.write_try_to_file(game.generate_number())
            tries_count += 1
            time.sleep(1)
            if tries_count > 1000:
                print "Something wrong"
                game_play = False
                break

    if game_mode == "server":
        game_play = True
        game = utility_functions.GameUtilityFunctions()
        utils = file_utilities.FileUtilities()
        tries_count = 0
        game.secret_number = game.generate_secret_number()
        print game.secret_number
        while game_play:
            lines = utils.read_from_file()
            if lines != None:
                guess_from_file = utils.get_guess(lines)
                print guess_from_file
            if guess_from_file != None:
                bk_to_write = game.return_bulls_cows_to_file(guess_from_file, game.secret_number)
                if bk_to_write != None:
                    if int(bk_to_write[0]) == 0 and int(bk_to_write[1]) == 5:
                            utils.write_try_to_file(bk_to_write)
                            print "Win"
                            game_play = False
                            sys.exit(0)
                            break
                    utils.write_try_to_file(bk_to_write)
            tries_count += 1
            time.sleep(1)
            if tries_count > 1000:
                print "Something wrong"
                game_play = False
                break
    exit()