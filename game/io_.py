# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import game_logic_functions

"""
Contains functions to work with I/O
"""


def read_from_file(file_to_read):
    """Read contents from given file

    :param str file_to_read: File to read
    :type file_to_read: str
    :return: file lines as list
    :rtype: list
    :raises TypeError: if the file_to_read is not a valid str
    """
    with open(file_to_read, 'r') as f:
        return f.read().strip().splitlines()



def get_answer(lines_from_file):
    """Extract amount of bulls and cows from given line list

    :param list lines_from_file: Lines to search for ansver in format of string containing 2 digits in range 0-5
    :type file_to_read: list
    :return: array of two elements
    :rtype: list
    :raises TypeError: if the lines_from_file is not a valid list
    """
    answer = lines_from_file[-1]
    if len(answer) < 5:
        answer_arr = [answer[0], answer[1]]
        print "cows", answer_arr[0]
        print "bulls", answer_arr[1]
        return answer_arr
        # print ("Something goes wrong")


def write_try_to_file(try_number, file_to_write):
    """Write random generated guess in file

    :param int try_number: Random generated integer to write in file
    :param str file_to_write: File to write
    :type try_number: int
    :type file_to_write: str
    """
    with open(file_to_write, 'a+') as f:
        f.write(str(try_number) + "\n")
    f.close()


def get_guess(lines_from_file):
    """Extract guess number from game file

    :param str lines_from_file: List of lines to search a guess
    :type lines_from_file: str
    :return: string from file
    :rtype: str
    """
    if len(lines_from_file) > 0:
        guess = lines_from_file[-1]
        if len(guess) > 3:
            return guess
