from turtle import *
left(90)
k = 20
for i in range(6):
    right(36)
    forward(10*k)
    right(36)
pu()
for x in range(16):
    for y in range(-10, 10):
        goto(x*k, y*k)
        dot(5)
done()
