from turtle import*
left(90)
k = 30
for i in range(8):
    forward(12*k)
    right(90)
pu()
for x in range(0,13):
    for y in range(0,13):
        goto(x * k, y * k)
        dot(4)
done()