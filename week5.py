def mymin(numbers):
    n = 0
    for i in numbers:
        print(i+1)


def find_longer(words, n):
    for i in range(len(words)):
        if len(words[i]) > n:
            return words[i]
    return words


def first_longer(words, n):
    for i in range(len(words)):
        if len(words[i]) > n:
            return words[i]
        else:
            return None
    return words


def histogram(numbers, char):
    result_char = 0
    for i in numbers:
        result_char = i * char
    return result_char




