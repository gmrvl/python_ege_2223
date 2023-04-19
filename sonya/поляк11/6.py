from turtle import *
left(90)
k = 30
x = 0
y = 0
for i in range(7):
    goto((x + 6) * k, (y - 9)*k)
    goto((x - 6) * k, (y + 2)*k)
    goto((x + 12) * k, (y + 3) * k)
pu()
for x in range(-15,15):
    for y in range(-15,15):
        goto(x * k,y * k)
        dot(4)
done()