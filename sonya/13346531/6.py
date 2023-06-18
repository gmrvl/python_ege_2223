from turtle import *
k = 30
left(90)
for i in range(10):
    forward(5 * k)
    right(60)
pu()
for x in range(-5,10):
    for y in range(-5,10):
        goto(x*k, y*k)
        dot(4)
done()