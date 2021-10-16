import random
import sys
import time

leettrans = {'a': ['4', '/-\\', '@', '/\\'],
             'b': ['8', '|3', '13'],
             'c': ['(', '{', '[', '<'],
             'd': ['[)', ')', '[}', '|)', '|}', '|>'],
             'e': ['3'],
             'f': ['|=', 'ph'],
             'g': ['6', '(_+'],
             'h': ['#', '|-|', ')-(', '/-/', '|~|'],
             'i': ['1', '!', '|', '][', ':'],
             'j': ['_|', 'u|', ';_[['],
             'k': ['|<', '|{'],
             'l': ['|', '1', '|_'],
             'm': ['/\\/\\', '|\\/|', '[\\/]', '(\\/)', '/V\\'],
             'n': ['/\\/', '|\\|', '(\\)', '/|/', '[\\]'],
             'o': ['0', '()', '[]', '<>', '*'],
             'p': ['|D', '|*', '|>'],
             'q': ['(_,)', '0,', 'O,', 'O\\', '[]\\'],
             'r': ['|2', '|?', '/2'],
             's': ['5', '$'],
             't': ['7', '+', '7`', '~|~', '†'],
             'u': ['(_)', '|_|', '/_/', '\\_/'],
             'v': ['\\/', '\\\\//'],
             'w': ['\\/\\/', '|/\\|', '[/\\]', '(/\\)', 'VV', '\\^/',
                   '1/\\/', '\\/1/', '1/1/'],
             'x': ['><', '}{', ')('],
             'y': ["'/", '%', '`/', '\\j'],
             'z': ['2', '7_'],
             }


def leet(string, prob):
    for c in string:
        if c.isalpha() is True:
            if random.random() <= prob:
                c = c.lower()
                string = string.replace(c, random.choice(leettrans[c]), 1)
    return string


def leet_loop(probability):
    while True:
        text = input('Please enter a word, no matter how short or long: ')
        if text == "":
            print('Let me sleep on it....')
            time.sleep(5)
            print('Sorry! No more leets this time, bye')
            sys.exit()
        print(leet(text, probability))


leet_loop(0.34)
