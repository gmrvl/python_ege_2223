from turtle import*
left(90)
k = 30
for i in range(4):
    forward(4*k)
    right(90)
    forward(8*k)
    right(90)
pu()
for x in range(9):
    for y in range(9):
        goto(x*k, y*k)
        dot(4)
done()