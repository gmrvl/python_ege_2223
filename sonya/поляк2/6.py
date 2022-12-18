from turtle import *

left(90)
k = 40
for i in range(12):
    forward(6 * k)
    right(120)
pu()
for x in range(10):
    for y in range(10):
        goto(x * k, y * k)
        dot(4)
done()
