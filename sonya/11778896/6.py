from turtle import*
left(90)
k = 30
for i in range(10):
    forward(5*k)
    right(60)
pu()
for x in range(15):
    for y in range(-7,15):
        goto(x * k, y * k)
        dot(4)
done()