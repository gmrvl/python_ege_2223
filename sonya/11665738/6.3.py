from turtle import*
left(90)
k = 30
for i in range(4):
    forward(14*k)
    right(120)
pu()
for x in range(-5,16):
    for y in range(-5,16):
        goto(x*k,y*k)
        dot(4)
done()