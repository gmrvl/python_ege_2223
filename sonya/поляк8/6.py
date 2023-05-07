from turtle import*
left(90)
k = 30
right(30)
for i in range(30):
    right(30)
    forward(3*k)
    right(30)
pu()
for x in range(8):
    for y in range(-5,5):
        goto(x*k, y*k)
        dot(4)
done()