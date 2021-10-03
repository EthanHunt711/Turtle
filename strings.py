def indef(text):
    vowel = ['a', 'e', 'o', 'u', 'i']
    i = text[0]
    if i in vowel:
        return 'an ' + text
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


def firstdigit(string):
    for i in string:
        if i.isdigit():
            return int(i)
    return 0


def numbers_for_uc(string):

    for index, character in enumerate(string):
        print(index, character)
        if character.isupper():
            string = string.replace(character, f'[{index}]', 1)
    return string


def grid(s):
    for i in range(len(s)):
        string = s[i:]+s[:i]
        print(string)

