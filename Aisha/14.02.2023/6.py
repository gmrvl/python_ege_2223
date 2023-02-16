from turtle import *

left(90)

k = 35
for i in range(4):
    forward(9 * k)
    right(90)

for i in range(3):
    forward(9 * k)
    right(120)
pu()
for x in range(0, 20):
    for y in range(0, 20):
        goto(x * k, y * k)
        dot(3)
done()
