from turtle import *
left(90)
k=30
for i in range(5):
    forward(8*k)
    right(60)
    forward(8*k)
    right(120)
penup()
for x in range(11):
    for y in range(15):
        goto(x*k,y*k)
        dot(5)
done()
