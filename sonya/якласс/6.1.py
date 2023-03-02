from turtle import*
left(90)
k = 30
for i in range(10):
    forward(3*k)
    right(90)
pu()
for x in range(11):
    for y in range(11):
        goto(x*k, y*k)
        dot(4)
done()