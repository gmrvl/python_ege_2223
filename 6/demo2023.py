from turtle import *
left(90)
for i in range(7):
    forward(10*30)  # умножили значение чтобы график был побольше
    right(120)
penup()
for x in range(11):
    for y in range(11):
        goto(x * 30, y * 30)
        dot(5)
done()
