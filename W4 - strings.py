def indef(text):
    first_letter = text[0]
    if first_letter == 'a' and 'e' and 'o' and 'u' and 'i':
        return 'an ' + text
    else:
        return 'a ' + text


def parens(string):
    string_2 = ''
    for letter in string:
        string_2 += f'({letter})'
    return string_2


def three_rays(string):
    count = 0
    for letter in string:
        count += 1
        print(letter + count*'-' + letter + count*'-' + letter)


def swap(s):
    if len(s) % 2 == 0:
        s_half = len(s)//2
        return s[s_half:]+s[:s_half]
    else:
        return s


def first_digit(string):
    string_char = []
    for letter in string:
        string_char.append(letter)
        if letter.isdigit():
            return letter
    else:
        return 0


def numbers_for_uc(string):
    new_string = ''
    for index, character in enumerate(string):
        if character.isupper():
            new_string += f'[{index}]'
        else:
            new_string += character
    return new_string


def grid(s):
    n = 0
    for i in s:
        while len(s):
            s.startwirh(n+i)
