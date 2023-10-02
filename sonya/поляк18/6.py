from turtle import *

k = 10
x = 0
y = 0
for i in range(10):
    x -= 6
    y += 9
    goto(x * k, y * k)
    x += 6
    y -= 2
    goto(x * k, y * k)
    x -= 3
    y -= 6
    goto(x * k, y * k)
pu()
for x in range(-40, 30):
    for y in range(-30, 30):
        goto(x * k, y * k)
        dot(4)
done()
