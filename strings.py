def indef(text):
    first_letter = text[0]
    if first_letter == 'a' and 'e' and 'o' and 'u' and 'i':
        return 'an ' + text
    else:
        return 'a ' + text
