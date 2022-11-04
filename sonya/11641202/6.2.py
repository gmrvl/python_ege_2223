from turtle import*
left(90)
k = 30
for i in range(5):
    forward(8*k)
    right(60)
    forward(8 * k)
    right(120)
pu()
for x in range(20):
    for y in range(20):
        goto(x*k, y*k)
        dot(4)
done()