from turtle import *
left(90)
for i in range(4):
    forward(12*25)
    right(90)
right(30)
for j in range(3):
    forward(8*25)
    right(60)
    forward(8*25)
    right(120)
pu()
for x in range(14):
    for y in range(14):
        goto(x*25,y*25)
        dot(5)
done()
