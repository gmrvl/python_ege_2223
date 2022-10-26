from turtle import *
left(90)
for i in range(4):
    forward(8*30)
    right(90)
    forward(8*30)
    right(90)
pu()
for x in range(11):
    for y in range(11):
        goto(x*30,y*30)
        dot(5)
done()