def outside_parens(string):
    output = ''
    inside_paren = False
    for i in string:
        if inside_paren:
            if i == ')':
                inside_paren = False
        else:
            if i == '(':
                inside_paren = True
            else:
                output = output + i
    return output


def has_all_digits(s):
    for d in '0123456789':
        if d not in s:
            return False
    return True


def find_pers_number():
    n = 0
    while not has_all_digits(str(n * n)):
        n = n + 1
    return n


def countmatch(s1, s2):
    for i, char in enumerate(s1):
        print(i, char)
        if char != s2[i]:
            return i
