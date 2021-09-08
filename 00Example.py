from turtle import *

n = 2


def spiral():
    reset()
    speed(40)
    pensize(2)
    pendown()
    for n in range(40):
        forward(n + (n + 10))
        left(90)


spiral()

done()
