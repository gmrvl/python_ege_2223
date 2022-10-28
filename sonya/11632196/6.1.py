from turtle import *
left(90)
k = 30
for i in range(8):
    forward(6*k)
    right(120)
pu()
for x in range(7):
    for y in range(7):
        goto(x*k, y*k)
        dot(4)
done()
