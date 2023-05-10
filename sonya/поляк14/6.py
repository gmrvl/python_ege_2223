from turtle import *
goto(0,0)
k = 30
x = 0
y = 0
for i in range(7):
    goto((x + 6) * k, (y - 9) * k)
    goto((x - 6) * k, (y + 2) * k)
    goto((x + 12) * k, (y + 3) * k)
pu()
goto(0,0)
for x in range(-10,19):
    for y in range(-10,19):
        goto(x*k, y * k)
        dot(4)
done()