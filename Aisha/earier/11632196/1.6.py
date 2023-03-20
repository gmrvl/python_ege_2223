from turtle import *

k = 30
left(90)
for i in range(6):
    forward(13 * k)
    right(120)

penup()
for x in range(1, 15):
    for y in range(1,15):
        goto(x * k, y * k)
        dot(4)
done()