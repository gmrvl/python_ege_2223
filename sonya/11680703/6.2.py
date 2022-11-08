from turtle import*

left(180)
k = 30
for i in range(12):
    right(60)
    forward(1*k)
    right(60)
    forward(1*k)
    right(270)
pu()
for x in range(-3,10):
    for y in range(-3,10):
        goto(x*k, y*k)
        dot(4)
done()