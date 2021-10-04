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
        print(n * char)


def allit(words):
    alliterate = True
    if len(words) == 0:
        return alliterate
    else:
        first_letter = words[0][:1]
        for w in words:
            if w.startswith(first_letter):
                alliterate = True
            elif len(words) == 1:
                alliterate = True
            else:
                alliterate = False
        return alliterate


