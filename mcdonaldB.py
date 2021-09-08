def print_verse(number, animal, sound):
    # it is possible to use new line instead of putting everyline
    # in a new print(), but for the sake of simplicity and avoiding
    # long lines I chose to do as follows
    print('Old MacDonald had a farm')
    print('E - I - E - I - O')
    print('And on this farm he had', number, animal)
    print('E - I - E - I - O')
    print('With a', sound, sound, 'here')
    print('And a', sound, sound, 'there')
    print('Here a', sound)
    print('there a', sound)
    print('Everywhere a', sound, sound)
    print('Old MacDonald had a farm')
    print('E - I - E - I - O')
    print()


def print_song():
    print_verse('a', 'cow', 'moo')
    print_verse('a', 'duck', 'quack')
    print_verse('some', 'chicks', 'cluck')


print_song()


