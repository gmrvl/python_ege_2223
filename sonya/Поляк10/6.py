from turtle import*
left(90)
k = 30
for i in range(11):
    forward(4*k)
    right(60)
pu()
for x in range(1,12):
    for y in range(1,12):
        goto(x*k, y*k)
        dot(4)
done()