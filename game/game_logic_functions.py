# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import io_
import random


def all_digits_are_unique(number):
    """Method to check duplicates

        Checks input number. If number not contains duplicate digits Return True, return False if no duplicates present.
        Example:

        >>> all_digits_are_unique(101)
        False
        >>> all_digits_are_unique(123)
        True

        number = 101 returns True
        number = 123 returns False

        :param number: Integer to be checked on duplicates.
        :return bool: Return False if no duplicates found. Return True if number contains duplicate digits.
        """
    num = str(number)
    if num.isdigit() == False:
        return False
    to_check = set(num)
    if len(to_check) < len(num):
        return False
    return True


def generate_numbers_list(number_len):
    """Generate list of numbers

        Generate list of fixed length numbers which did not contain duplicate digits
        i.e [12345, 12346, 65783, ...]

        :param number_len: Integer input parameter - length of numbers inside generated list
        :return numbers_list: Return List of integers
        """
    numbers_list = []
    if number_len > 0:
        for i in range(10 ** (number_len - 1), 10 ** number_len - 1, 1):
            if all_digits_are_unique(i):
                numbers_list.append(i)
        return numbers_list


def analyze_bulls_cows_and_remove_number_list(bk_get_from_file, number_from_file, numbers_list):
    """Compare bulls&cows for number which came from file
    and bulls&cows for every number that present in numbers_list
    If bulls&cows for number from number_list doesn't equal to bulls&cows for number_from_file this number removes from list.

    :param bk_get_from_file: string of two elements that represents bulls&cows count i.e "12"
    :type bk_get_from_file: str
    :param number_from_file: string that represent latest guess try from file to compare i.e "12345"
    :type number_from_file: str
    :param numbers_list: list of elements which contain all possible guesses based on initial number length
    :type numbers_list: list
    :return: modified numbers list
    :rtype: list
    """
    my_current_try = str(number_from_file)
    list_to_iterate = []
    for num_from_list_to_compare in numbers_list:
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
        if cows != int(bk_get_from_file[0]) or bulls != int(bk_get_from_file[1]):
            list_to_iterate.append(num_from_list_to_compare)
    if len(list_to_iterate) > 0:
        for elem in list_to_iterate:
            numbers_list.remove(elem)
    return numbers_list


def generate_secret_number(numbers_list):
    """Generates random number from list of numbers and use it as a secret number to guess

    :param numbers_list: list of pre-generated numbers of fixed length
    :type numbers_list: list
    :return: random number from numbers_list
    :rtype: int
    """
    if len(numbers_list) > 0:
        rand_i = random.randint(0, len(numbers_list))
        secret_number = numbers_list[rand_i]
        return secret_number


def return_bulls_cows_to_file(try_from_file, secret_number):
    """Calculate bulls&cows for try_from_file compared to secret_number.

    :param try_from_file: latest guess from file
    :type try_from_file: int
    :param secret_number: secret number to guess
    :type secret_number: int
    :return: string which represents bulls&cows
    :rtype: string
    """
    bulls = 0
    cows = 0
    try_num_to_str = str(try_from_file)
    secret_num_to_str = str(secret_number)
    for i in range(0, len(try_num_to_str), 1):
        for j in range(0, len(secret_num_to_str), 1):
            if try_num_to_str[i] == secret_num_to_str[j]:
                if i == j:
                    bulls = bulls + 1
                else:
                    cows = cows + 1
    return str(cows) + str(bulls)


def generate_number(list_of_numbers):
    """Generate random number from list_list_of_numbers and use it as a guess

    :param numbers_list: list of pre-generated numbers of fixed length
    :type numbers_list: list
    :return: random number from numbers_list
    :rtype: int
    """
    if len(list_of_numbers) > 1:
        rand_i = random.randint(0, len(list_of_numbers) - 1)
        try_to_file = list_of_numbers[rand_i]
        return try_to_file
    else:
        return list_of_numbers[0]

if __name__ == "__main__":
    import doctest
    doctest.testmod()