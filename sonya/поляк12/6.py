from turtle import*
left(90)
k = 30
right(45)
for i in range(9):
    forward(9 * k)
    right(90)
pu()
for x in range(0,15):
    for y in range(-7,10):
        goto(x*k, y*k)
        dot(4)
done()