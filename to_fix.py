def outside_parens(string):
    output = ''
    inside_paren = False
    for i in string:
        if inside_paren:
            if string[i] == ')':
                inside_paren = False
        else:
            if string[i] == '(':
                inside_paren = True
            else:
                output = output + string[i]
    return output


def has_all_digits(s):
    for d in '0123456789':
        # print(d)
        if d not in s:
            return False
    return True



def find_pers_number():
    while not has_all_digits(n*n):
        n = n + 1
    return n


def countmatch(s1, s2):
    for i, char in enumerate(s1):
        if char != s2[i]:
            return i
