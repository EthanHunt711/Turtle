import random


def game():
    count_guess = 0
    secret_num = random.randrange(1, 99, 1)
    guess_num = "Let's play a fun game! \nI have thought of number between 1 and 99 \nDo you think you can guess what my secret number is? "
    next_guess = 'please guess again! '
    low_guess = 'That is too low'
    high_guess = 'That is too high'
    correct_guess = 'Congratulations! That is correct'
    good_guess = 'That is really good'
    after_four_guesses = 'You can do better!'
    bad_guess = 'It took you a long time but you made it at last'

    guess = int(input(guess_num))

    while guess != secret_num:
        count_guess += 1
        if guess < secret_num:
            print(low_guess)
            guess = int(input(next_guess))

        elif guess > secret_num:
            print(high_guess)
            guess = int(input(next_guess))
    else:
        print(correct_guess)
        print('You made it in', count_guess, 'guesses.')
        evaluation(count_guess)


def evaluation(number):
    good_guess = 'That is really good'
    after_four_guesses = 'You can do better!'
    bad_guess = 'It took you a long time but you made it at last'

    if number <= 3:
        print(good_guess)

    elif number > 4 < 6:
        print(after_four_guesses)

    elif number > 6:
        print(bad_guess)


