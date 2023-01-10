from turtle import*
left(90)
k = 40
for i in range(4):
    forward(12*k)
    right(90)
right(30)
for l in range(3):
    forward(8*k)
    right(60)
    forward(8 * k)
    right(120)
pu()
for x in range(15):
    for y in range(15):
        goto(x*k, y*k)
        dot(4)
done()