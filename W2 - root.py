def find_root(number):
    guess = 1.0
    for x in range(1, 11):
        guess = ((number / guess) + guess) / 2
        print('After iteration', x, 'my guess is', guess)


def main():
    user_guess = float(input("please enter a random number: "))
    find_root(user_guess)


main()
