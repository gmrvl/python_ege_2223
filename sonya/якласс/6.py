from turtle import*
left(90)
k = 30
for i in range(6):
    forward(4*k)
    right(60)
pu()
for x in range(8):
    for y in range(-6,8):
        goto(x*k, y*k)
        dot(4)
done()
