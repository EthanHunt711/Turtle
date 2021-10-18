import random
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
    out_l = []
    for i, c in enumerate(string):
        if c.lower() in leettrans.keys():
            if random.random() <= prob:
                c = random.choice(leettrans[string[i].lower()])
        out_l.append(c)
    return ''.join(out_l)


def leet_loop(probability):
    while True:
        text = input('Please enter a text, no matter how short or long: ')
        if text == "":
            print('Let me sleep on it....')
            time.sleep(5)
            print('Sorry! No more leets this time, bye')
            break
        print(leet(text, probability))


leet_loop(0.34)
