from turtle import *
left(90)
for i in range(8):
    forward(6*30)
    right(120)
pu()
for x in range(11):
    for y in range(11):
        goto(x*30,y*30)
        dot(5)
done()