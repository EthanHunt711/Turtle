def mymin(numbers):
    # numbers.sort()
    first_min = numbers[0]
    for i in range(len(numbers)):
        if numbers[i] < first_min:
            first_min = numbers[i]
    return first_min


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


def allit(words):
    letter = words[0]
    for x in range(len(words)):
        if

