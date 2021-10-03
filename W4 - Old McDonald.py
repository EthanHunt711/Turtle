from strings import indef


def print_verse(animal, sound):
    # it is possible to use new line instead of putting everyline
    # in a new print(), but for the sake of simplicity and avoiding
    # long lines I chose to do as follows
    print('Old MacDonald had a farm')
    print('E - I - E - I - O')
    print(f"And on this farm he had {indef(animal)}")
    print('E - I - E - I - O')
    print(f"With {indef(sound)}", sound, 'here')
    print(f"And {indef(sound)}", sound, 'there')
    print(f'Here {indef(sound)}')
    print(f'There {indef(sound)}')
    print(f'Everywhere {indef(sound)}')
    print('Old MacDonald had a farm')
    print('E - I - E - I - O')
    print()


def print_song():
    print_verse('cow', 'moo')
    print_verse('duck', 'quack')
    print_verse('chick', 'cluck')
    print_verse('owl', 'uou')

print_song()
