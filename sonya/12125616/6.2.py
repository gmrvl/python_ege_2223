from turtle import*
left(90)
k = 30

for i in range(4):
    forward(5*k)
    right(90)
    forward(7*k)
    right(90)
pu()

for x in range(10):
    for y in range(10):
        goto(x*k, y*k)
        dot(4)
done()
