from turtle import *

k = 30
left(90)
for i in range(7):
    forward(10*k)
    right(120)

penup()
for x in range(15):
    for y in range(15):
        goto(x*k, y*k)
        dot(4)
done()
