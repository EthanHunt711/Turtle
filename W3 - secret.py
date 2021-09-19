def secret_number():
    secret_num = 28
    guess_num = int(input('what is your guess? '))
    next_guess = int(input('please guess again! '))
    guess_list = []
    guess_list.append(guess_num)
    guess_list.append(next_guess)
    print(guess_num)
    while guess_num != secret_num:
        if guess_num < secret_num:
            print('that is too low')
            print(next_guess)
            break
        else:
            print('that is too high')
            print(next_guess)
            break
    if guess_num == secret_num:
        print('congratulations, that is correct!')
        print('You made it in', len(guess_list), 'guesses.')
        print('That is really good!')

secret_number()