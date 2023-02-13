from turtle import*
left(90)
k = 30
for i in range(4):
    forward(12*k)
    right(150)
    forward(12*k)
    right(30)
pu()
for x in range(14):
    for y in range(-14, 14):
        goto(x*k, y*k)
        dot(4)
done()