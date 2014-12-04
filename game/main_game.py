# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import io_
import game_logic_functions
import time
import sys
import io_

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    gamefile = "game.txt"
    game_number_length = 5
    numbers_list = []
    try_to_file = 0
    bk_get_from_file = [0, 0]
    secret_number = 0
    print "Please select game mode.\n" \
          "Available modes - Server and Client.\n" \
          "Choose Server if you want program to guess the number, read opponent assumptions from file and reply to file with count of Bulls and Cows.\n" \
          "Choose Client if you want program to guess secret number by sending tries to file and processing bulls and cows in response.\n" \
          "" \
          "If you want a game to play with itself you can run two copies with different modes in the same directory." \
          "Please choose mode:"
    game_mode = raw_input()
    if game_mode == "client":
        game_play = True
        numbers_list = game_logic_functions.generate_numbers_list(game_number_length)
        tries_count = 0
        try_to_file = game_logic_functions.generate_number(numbers_list)
        io_.write_try_to_file(try_to_file, gamefile)
        while game_play:
            if len(numbers_list) > 0:
                lines = io_.read_from_file(gamefile)
                bk_get_from_file = io_.get_answer(lines)
                if bk_get_from_file != None:
                    numbers_list = game_logic_functions.analyze_bulls_cows_and_remove_number_list(
                        bk_get_from_file, try_to_file, numbers_list)
                    print len(numbers_list)
                    if int(bk_get_from_file[0]) == 0 and int(bk_get_from_file[1]) == 5:
                        print "Win", try_to_file
                        game_play = False
                        sys.exit(0)
                        break
                    try_to_file = game_logic_functions.generate_number(numbers_list)
                    io_.write_try_to_file(try_to_file, gamefile)
            tries_count += 1
            time.sleep(1)
            if tries_count > 1000:
                print "Something wrong"
                game_play = False
                break

    if game_mode == "server":
        game_play = True
        tries_count = 0
        numbers_list = game_logic_functions.generate_numbers_list(game_number_length)
        secret_number = game_logic_functions.generate_secret_number(numbers_list)
        print secret_number
        while game_play:
            lines = io_.read_from_file(gamefile)
            if lines != None:
                guess_from_file = io_.get_guess(lines)
                if guess_from_file != None:
                    print guess_from_file
                else:
                    print "No new response"
            if guess_from_file != None:
                bk_to_write = game_logic_functions.return_bulls_cows_to_file(guess_from_file, secret_number)
                if int(bk_to_write[0]) == 0 and int(bk_to_write[1]) == 5:
                        io_.write_try_to_file(bk_to_write, gamefile)
                        print "Win"
                        game_play = False
                        sys.exit(0)
                        break
                io_.write_try_to_file(bk_to_write, gamefile)
            tries_count += 1
            time.sleep(1)
            if tries_count > 1000:
                print "Something wrong"
                game_play = False
                break
    exit()