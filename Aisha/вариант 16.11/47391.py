from turtle import *

k = 20

left(90)
for i in range(14):
    right(60)
    forward(2*k)
    right(60)
    forward(2*k)
    right(270)
penup()
for x in range(-5, 10):
    for y in range(-15, 5):
        goto(x*k, y*k)
        dot(5)
done()
