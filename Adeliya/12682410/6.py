from turtle import *
left(90)
k=30
for i in range(10):
    forward(5*k)
    right(60)
pu()
for x in range(11):
    for y in range(-10,11):
        goto(x*k,y*k)
        dot(5)
done()