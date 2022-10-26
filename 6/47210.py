from turtle import *

k = 30
left(90)
# back(100)
for i in range(7):
    forward(10*k)
    right(120)

penup()
for x in range(11):
    for y in range(11):
        goto(x*k, y*k)
        dot(5)
done()
