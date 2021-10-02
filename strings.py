def indef(text):
    first_letter = text[0]
    if first_letter == 'a' or 'e' or 'o' or 'u' or 'i':
        return 'an ' + text
    else:
        return 'a ' + text


def parens(string):
    result = ''
    for char in string:
        result = result + f'({char})'
    return result


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
    for letter in string:
        if letter.isdigit():
            return letter
    return 0


def numbers_for_uc(string):

    for index, character in enumerate(string):
        if character.isupper():
            string = string.replace(character, f'[{str(index)}]')
    return string


def grid(s):
    for i in range(len(s)):
        string = s[i:]+s[:i]
        print(string)

