from turtle import*
left(90)
k = 30
for n in range(15):
    forward(4*k)
    right(60)
pu()
for x in range(0,20):
    for y in range(0,20):
        goto(x*k, y *k)
        dot(4)
done()