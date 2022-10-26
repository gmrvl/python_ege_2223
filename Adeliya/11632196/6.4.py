from turtle import *
left(90)
for i in range(6):
    right(36)
    forward(10*20)
    right(36)
pu()
for x in range(16):
    for y in range(10):
        goto(x*20,y*20)
        dot(5)
done()
