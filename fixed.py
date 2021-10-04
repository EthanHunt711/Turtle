def outside_parens(string):
    output = ''
    inside_paren = False
    for char in string:
        if inside_paren:
            if char == ')':
                inside_paren = False
        else:
            if char == '(':
                inside_paren = True
            else:
                output = output + char
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
        s1 = s1.lower()
        s2 = s2.lower()
        if (len(s1) > 0) and (len(s2) > 0):
            if char != s2[i]:
                return i
            elif s1 == s2:
                return len(s1)
            elif s2.startswith(s1):
                return len(s1)
            elif s1.startswith(s2):
                return len(s2)
        else:
            return None




