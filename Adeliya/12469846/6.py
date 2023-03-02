from turtle import *
left(90)
k=30
for i in range(4):
    forward(9*k)
    right(90)
for i in range(3):
    forward(9*k)
    right(120)
pu()
for x in range(11):
    for y in range(11):
        goto(x*k,y*k)
        dot(5)
done()