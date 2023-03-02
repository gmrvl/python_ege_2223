from turtle import *
left(90)
k=30
for i in range(6):
    left(120)
    forward(6*k)
pu()
for x in range(-11,2):
    for y in range(-11,11):
        goto(x*k,y*k)
        dot(5)
done()