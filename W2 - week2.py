def num_lengths():
    for numbers in range(2, 100):
        print(numbers, 'raised to 10 has', len(str(numbers ** 10)), 'digits: ', numbers ** 10)


def check_numbers(n, m):
    if n == m:
        print('the numbers are the same')

    if n % 2 == 1:
        print('the first number is odd')

    if m < 0:
        print('the second number is negative')

    if n > 99 and m > 99:
        print('both numbers are big')


def f(x):
    if x <= 10:
        return 1
    else:
        return x / 10


def g(x):
    if x <= 2 or x >= 10:
        return 0
    elif 2 <= x <= 5:
        return (x - 2) / 3
    elif 5 <= x <= 10:
        return (10 - x) / 5


def sum_squares(n):
    total = 0
    # n = input(int('please enter a valid number: '))
    for i in range(n + 1):
        total += i ** 2
    return total


def two_dice():
    for n in range(1, 7):
        for x in range(1, 7):
            print('Red die is', n, 'and blue die is', x, 'giving', n + x)


check_numbers(101, 101)
