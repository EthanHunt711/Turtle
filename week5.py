def mymin(numbers):
    numbers.sort()
    return numbers[0]


def find_longer(words, n):
    for i in words:
        if len(i) > n:
            return i
    else:
        return None


def histogram(numbers, char):
    for n in numbers:
        result = n * char
        print(result)


def allit(words):
    alliterate = True
    if len(words) == 0:
        alliterate = True
    elif len(words) == 1:
        alliterate = True
    elif len(words) > 1:
        first_letter = words[0][:1]
        for l in words:
            if l.startswith(first_letter):
                alliterate = True
            else:
                alliterate = False
    return alliterate


def anti_allit(words):
    first_letter = words[0][:1]
    for l in words:
        if not l.startswith(first_letter):
            return True
    return False


def addpairs(numbers):
    result = []
    for i, n in enumerate(numbers):
        for i in numbers:
            if i < (len(numbers)-1):
                result.append(n + numbers[i+1])
    print(result)


def endings(words):
    endings_list = [words]
    for c in words:
        if len(words) > 0:
            words = words.strip(words[:1])
            endings_list.append(words)
    return endings_list


def vhistogram(numbers, char):
    print ('no')


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







