
from turtle import*
left(90)
k = 30
for i in range(14):
    right(60)
    forward(2 * k)
    right(60)
    forward(2 * k)
    right(270)
pu()
for x in range(-10, 13):
    for y in range(-16,5):
        goto(x * k, y * k)
        dot(4)
done()