def num_lengths():
    for numbers in range(2, 100):
        print(numbers, 'raised to 10 has', len(str(numbers ** 10)), 'digits: ', numbers ** 10)


def check_numbers():
    n = int(input('please enter the first number: '))
    m = int(input('please enter the second number: '))
    if n == m:
        print('the numbers are the same')
    elif n % 2 == 1:
        print(n, 'is an odd number')
    elif n < 0:
        print(m, 'is a negative number')
    elif n > 99 and m > 99:
        print('both numbers are big')
    else:
        print()


def f(x):
    if x <= 10:
        return 1
    else:
        return x / 10


def g(x):
    if x <= 2:
        return 0
    elif 2 <= x <= 5:
        return (x - 2) / 3
    elif 5 <= x <= 10:
        return (10 - x) / 5
    elif x >= 10:
        return 0
    else:
        return


def sum_squares(n):
    total = 0
    # n = input(int('please enter a valid number: '))
    for i in range(n + 1):
        total += i ** 2
    print(total)


def two_dice():
    for n in range(1, 7):
        for x in range(1, 7):
            print('Red dice is', n, 'and blue dice is', x, 'giving', n + x)



