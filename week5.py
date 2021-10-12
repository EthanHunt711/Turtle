def mymin(numbers):
    numbers.sort()
    return numbers[0]


def find_longer(words, n):
    long_ws = []
    for w in words:
        if len(w) > n:
            long_ws.append(w)
    return long_ws


def first_longer(words, n):
    for w in words:
        if len(w) > n:
            return w
    else:
        return None


def histogram(numbers, char):
    for n in numbers:
        result = n * char
        print(result)


def allit(words):
    if len(words) <= 1:
        return True
    else:
        first_letter = words[0][0].lower()
        i = 0
        for w in words:
            w = w.lower()
            print(w[0])
            if w[0] != first_letter:
                return False
        return True


def anti_allit(words):
    first_letter = words[0][:1]
    for l in words:
        if not l.startswith(first_letter):
            return True
    return False


def addpairs(numbers):
    result = []
    for i, n in enumerate(numbers):
        if i+1 <= len(numbers):
            cum_num = n + numbers[i+1]
            result.append(cum_num)
    return ''.join(result)


def endings(words):
    endings_list = [words]
    for c in words:
        if len(words) > 0:
            words = words.strip(words[:1])
            endings_list.append(words)
    return endings_list


def vhistogram(numbers, char):
    v_result = []
    for n in numbers:
        result = n * char
        v_result.append((max(numbers)-n) * " ")
        v_result.append(result)
    for c in range(len(v_result)):
        for x in v_result:
            print(x[c-1:c], end=' ')
        print()


def procrustean(numbers, low, high):
    for i, n in enumerate(numbers):
        if n < low:
            numbers[i] = low
        elif n > high:
            numbers[i] = high
    return numbers


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








