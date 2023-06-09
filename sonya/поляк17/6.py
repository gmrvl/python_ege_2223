from turtle import *
left(90)
k = 10
forward(200)
for i in range(10):
    right(90)
    forward(50*k)
pu()
for x in range(0,50):
    for y in range(-50,50):
        goto(x*k, y*k)
        dot(4)
done()