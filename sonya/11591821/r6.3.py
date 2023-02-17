from turtle import *
left(90)
k = 20
for i in range(6):
    forward(10*k)
    right(60)
pu()
for x in range(20):
    for y in range(-10,20):
        goto(x*k,y*k)
        dot(4)
done()