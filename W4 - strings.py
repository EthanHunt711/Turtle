def indef(text):
    first_letter = text[0]
    if first_letter == 'a' and 'e' and 'o' and 'u' and 'i':
        return 'an ' + text
    else:
        return 'a ' + text


def parens(string):
    for letter in string:
        print('('+letter+')')


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
    letter_list = []
    for letter in string:
        letter_list.append(letter)
        if letter.isdigit():
            return letter
            break
        else:
            return 0


