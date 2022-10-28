from turtle import*

left(90)
k = 25
for i in range(4):
    forward(10*k)
    right(60)
    forward(10*k)
    right(120)
pu()
for x in range(-3,20):
    for y in range(-3,20):
        goto(x*k, y*k)
        dot(4)
done()