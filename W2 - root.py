def find_root(number):
    for x in range(1, 11):
        guess = 1.0
        guess = (number + guess / guess) / 2
        print('after iteration', x, 'my guess is', guess)


def main():
    user_guess = float(input('please enter a random number:'))
    print(find_root(user_guess))


find_root(19.9)
