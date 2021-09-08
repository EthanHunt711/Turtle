from turtle import *


# a function to draw a spiral consisting of 400 lines

def spiral():
    reset()
    speed(40)
    pensize(2)
    pendown()
    for n in range(40):
        forward(n + (n + 10))
        left(90)


# a function to draw a spiral consisting of 400 lines with a given angle
def spiral_2(angle):
    reset()
    speed(40)
    pendown()
    for n in range(400):
        # pendown()
        left(angle)
        forward(n)


# a function to draw a spiral consisting of 400 lines with parameters such as angle and line color
def spiral_3(number_rotation, angle, color):
    reset()
    speed(40)
    for n in range(number_rotation):
        pendown()
        pencolor(color)
        left(angle)
        forward(n)


spiral()
# spiral_2(90)
# spiral_3(500, 135, 'green')

done()
