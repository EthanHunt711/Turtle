import random


def odd_part(n):
    while n % 2 == 0:
        print(n)
        n = n / 2
        if n % 2 != 0:
            print(n)


def count_rand(limit):
    total = 0
    n = random.Random()
    while total < limit:
        print(n)
        total += n
        if total >= limit:
            print(n)
            break


def first_short(words):
    for short_word in words:
        if len(short_word) < 5:
            print(short_word)
            break


# first_short(['cheetah', 'mongoose', 'bat', 'fox'])
count_rand(4)