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
        for w in words:
            w = w.lower()
            if w[0] != first_letter:
                return False
        return True


def anti_allit(words):
    if len(words) <= 1:
        return True
    else:
        first_letter_list = []
        for w in words:
            w = w.lower()
            first_letter_list.append(w[0])
        for char in first_letter_list:
            if first_letter_list.count(char) > 1:
                return False
        return True


def addpairs(numbers):
    sum = 0
    result = []
    for n in numbers:
        for i in numbers[numbers.index(n)+1:]:
            sum = n + i
            result.append(sum)
    return result


def endings(words):
    endings_list = []
    if len(words) < 1:
        return []
    else:
        endings_list.insert(0, words)
        for c in range(len(words)-1):
            words = words.strip(words[0])
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

def vhistogramO(numbers, char):
    v_line = []
    for n in numbers:
        v_line.append(((max(numbers)-n) * " ") + (n * char))
    for c in range(len(v_line)):
        for l in v_line:
            print(l[c-1:c], end=' ')
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
    startchars = []
    endchars = []
    result = []
    for s in strings:
        startchars.append(s[0])
        endchars.append(s[-1])
    for s in strings:
        for c in s[1:-1]:
            if c not in startchars and c not in endchars:
                result.append(c)
    return ''.join(sorted(set(result)))








