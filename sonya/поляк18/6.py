from turtle import*

k = 30
x = 0
y = 0
for i in range(10):
    goto((x - 6)*k,(y + 9)*k )
    goto((x + 6) * k, (y - 2) * k)
    goto((x - 3) * k, (y - 6) * k)
pu()
for x in range(-7,30):
    for y in range(-7,30):
        goto(x*k, y*k)
        dot(4)
done()
