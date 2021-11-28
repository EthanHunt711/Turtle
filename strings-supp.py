def wordtriangle(word):
    i = 0
    for i in range(len(word)):
        print(word[:i + 1])


def underline_upper(line):
    print(line)
    new_line = ''
    for c in line:
        if c.isupper():
            new_line += '='
        else:
            new_line += ' '
    print(new_line)


def dup_some(string, to_duplicate):
    new_string = ''
    for char in string:
        if char in to_duplicate:
            new_string += char * 2
        else:
            new_string += char
    return new_string


def stairs(string):
    i = 0
    for i in range(len(string) - 2):
        print(f'{i * " "}{string[i:i + 3]}')


def upcase_firsts(s):
    out = ''
    make_upper = True
    for char in s:
        if make_upper:
            out += char.upper()
        else:
            out += char
        if char == ' ':
            make_upper = True
        else:
            make_upper = False
    return out


def split(string):
    line = ''
    for char in string:
        if char == ' ':
            print(line)
            line = len(line) * ' '
        else:
            line += char
    print(line)