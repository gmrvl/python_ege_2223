from turtle import *
left(90)
k=20
for i in range(4):
    forward(8*k)
    right(90)
for j in range(3):
    forward(12*k)
    right(120)
pu()
for x in range(11):
    for y in range(15):
        goto(x*k,y*k)
        dot(5)
done()