from turtle import *


# missing function is added

def circle_pattern():
    reset()
    speed(10)  # max speed
    for radius in range(20, 40):
        pendown()
        circle(radius)
        penup()
        forward(1.8 * radius)
        left(20)


def square_pattern():
    reset()
    speed(20)  # max speed
    pencolor('orange')
    fillcolor('blue')
    for _ in range(4):
        pendown()
        circle_of_squares(20)
        penup()
        forward(170)
        pendown()
        begin_fill()
        circle(20)
        end_fill()
        penup()
        left(80)
        forward(100)


def circle_of_squares(n):
    # 15 squares because there is a turn 24 degrees between each,
    # and 15*24 = 360, a full circle
    # the angle of the next square is dependant on the number of squares
    speed(60)
    for _ in range(n):
        square()
        penup()
        forward(30)
        left(360/n)
        pendown()


# a function for drawing a square was missing
def square():
    # code is replaced with a for-loop
    for _ in range(4):
        left(90)
        forward(50)


# square_pattern()
circle_of_squares(30)

done()
