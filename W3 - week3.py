import random


def odd_part(n):
    while n % 2 == 0:
        n = n // 2
    else:
        n
    return n


def count_rand(limit):
    total = 0
    n = random.random()
    random_numbers_count = 0
    while total < limit:
        random_numbers_count += 1
        total += n
        if total >= limit:
            total

    return random_numbers_count


def first_short(words):
    for short_word in words:
        if len(short_word) < 5:
            return short_word




