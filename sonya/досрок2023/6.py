from turtle import*
left(90)
k = 23
right(315)
for i in range(7):
    forward(16*k)
    right(45)
    forward(8*k)
    right(135)
pu()
for x in range(-13,13):
    for y in range(0,20):
        goto(x*k,y*k)
        dot(4)
done()