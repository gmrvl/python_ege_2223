from turtle import *
left(90)
k=25
for i in range(14):
    right(60)
    forward(2*k)
    right(60)
    forward(2*k)
    right(270)
penup()
for x in range(-5, 15):
    for y in range(-16,11):
        goto(x*k,y*k)
        dot(5)
done()