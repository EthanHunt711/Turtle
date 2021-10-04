def mymin(numbers):
    min = 0
    for n in numbers:
        print(n)
        if [n] < [n+1]:
            min = n
        return min


def find_longer(words, n):
    for i in words:
        if len(i) > n:
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




