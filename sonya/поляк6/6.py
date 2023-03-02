from turtle import *
print(17*15)
x = 0
y = 0
k = 45
for i in range(1):
    x += 10
    y += 10
    goto(x*k, y*k)
    x += 3
    y -= 6
    goto(x*k, y*k)
    x -= 9
    y += 3
    goto(x*k, y*k)
pu()
goto(0,0)
for x in range(0, 15):
    for y in range(0,15):
        goto(x * k, y * k)
        dot(3)
done()
