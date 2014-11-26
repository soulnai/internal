Bulls&Cows
=======================

Program
-------

*Overview

    This program designed to play game Bulls&Cows trough the text file. Run from console. It can work in two modes:
        - Server - generate the secret number, listen for tries in file, and generate response after analyze try and secret number match.
        - Client - try to guess secret number by sending guesses to file, get response and work with them to generate new guess.

    If you want a game to play with itself you can run two copies with different modes in the same directory.

    In the game directory should be an empty text file named game.txt in UTF-8 without BOM encoding.