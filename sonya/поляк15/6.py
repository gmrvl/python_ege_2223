from turtle import*
goto(0,0)
k = 30
x = 0
y = 0
for i in range(3):
    goto((x + 10) * k, (y + 10) * k)
    goto((x + 3) * k, (y - 6) * k)
    goto((x - 9) * k, (y + 3) * k)
pu()
goto(0,0)
for x in range(-10,20):
    for y in range(-10,20):
        goto(x * k, y * k)
        dot(4)
done()