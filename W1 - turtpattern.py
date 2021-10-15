from turtle import *


def circle_pattern():
    reset()
    speed(10)                   # max speed
    for radius in range(20, 40):
        pendown()
        circle(radius)
        penup()
        forward(1.8 * radius)
        left(20)
        

def square_pattern():
    reset()
    speed(10)                   # max speed
    pencolor('blue')
    fillcolor('red')
    for _ in range(6):
        pendown()
        circle_of_squares()
        penup()
        forward(130)
        pendown()
        begin_fill()
        circle(20)
        end_fill()
        penup()
        left(80)
        forward(100)


def circle_of_squares():
    # 15 squares because there is a turn 24 degrees between each,
    # and 15*24 = 360, a full circle
    for _ in range(15):
        square(20)
        penup()
        forward(30)
        left(24)
        pendown()

circle_pattern()

done
