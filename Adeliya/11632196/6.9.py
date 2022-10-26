from turtle import *
left(90)
for i in range(4):
    forward(10*25)
    right(90)
right(90)
for j in range(5):
    forward(6*25)
    left(60)
    forward(6*25)
    left(120)
pu()
for x in range(14):
    for y in range(14):
        goto(x*25,y*25)
        dot(5)
done()