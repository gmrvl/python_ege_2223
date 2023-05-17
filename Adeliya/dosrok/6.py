from turtle import *
left(90)
k=20
right(315)
for i in range(7):
    forward(16*k)
    right(45)
    forward(8*k)
    right(135)
penup()
for x in range(-15,10):
    for y in range(20):
        goto(x*k,y*k)
        dot(5)
done()