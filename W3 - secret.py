import random


def secret_number():
    count_guess = 0
    secret_num = random.randrange(1, 99, 1)
    guess_num = 'what is your guess? '
    next_guess = 'please guess again! '
    low_guess = 'That is too low'
    high_guess = 'That is too high'
    correct_guess = 'Congratulations! That is correct'
    good_guess = 'That is really good'
    after_four_guesses = 'You can do better!'
    bad_guess = 'It took you a long time but you made it at last'

    guess = int(input(guess_num))

    while guess:
        count_guess += 1
        if guess < secret_num:
            print(low_guess)
            guess = int(input(next_guess))

        elif guess > secret_num:
            print(high_guess)
            guess = int(input(next_guess))
        elif guess == secret_num:
            print(correct_guess)
            print('You made it in', count_guess, 'guesses.')
            if count_guess <= 3:
                print(good_guess)
                break
            elif count_guess > 4 < 6:
                print(after_four_guesses)
                break
            elif count_guess > 6:
                print(bad_guess)
                break


def game():
    secret_number()


game()
