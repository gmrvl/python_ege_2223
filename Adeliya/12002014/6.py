from turtle import *
left(90)
k=40
for i in range(12):
    right(60)
    forward(1*k)
    right(60)
    forward(1*k)
    right(270)
pu()
for x in range(-7,7):
    for y in range(-9,6):
        goto(x*k,y*k)
        dot(5)
done()