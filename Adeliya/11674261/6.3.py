from turtle import *
left(90)
k=20
for i in range(6):
    forward(13*k)
    right(120)
pu()
for x in range(15):
    for y in range(15):
        goto(x*k,y*k)
        dot(5)
done()