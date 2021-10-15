def progress(string):
    words = string.split()
    record = 0
    found = []
    for word in words:
        if len(word) > record:
            found.append(word)
            record = len(word)
    return '->'.join(found)


def midchars(strings):
    first_last_chars = []
    # endchars = []
    result = []
    for s in strings:
        first_last_chars.append(s[0])
        first_last_chars.append(s[-1])
        for c in s[1:-1]:
            print(s[1:-1])
            if c not in first_last_chars:
                print(c)
                result.append(c)
        print(first_last_chars)

    return ''.join(sorted(result))


