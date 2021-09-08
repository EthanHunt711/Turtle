def sum_of_sequence():
    # asks the user to allocate the number of numbers in the loop
    number = input('Please write how many numbers you would like to add to one another: ')
    # converting the user's input into an integer
    number = int(number)

    # declaring the initial value of the parameter
    total = 0
    # for loop to calculate the range
    for i in range(number):
        print(i)
        # getting the sum of numbers in the range
        total += i

    print('the total sum of numbers generated is: ', total)


sum_of_sequence()
