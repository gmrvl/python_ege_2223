from turtle import *
left(90)
k=30
for i in range(6):
    right(36)
    forward(10*k)
    right(36)
pu()
for x in range(18):
    for y in range(-11,11):
        goto(x*k,y*k)
        dot(5)
done()