from turtle import *
left(90)
k = 30
for i in range(4):
    forward(8*k)
    right(90)
for i in range(3):
    forward(12*k)
    right(120)
pu()
for x in range(-10,10):
    for y in range(-10, 10):
        goto(x*k, y*k)
        dot(4)
done()