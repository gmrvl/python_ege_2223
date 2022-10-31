from turtle import*

left(90)
k = 30
for i in range(4):
    forward(10 * k)
    right(90)
for t in range(5):
    forward(6 * k)
    right(60)
    forward(6 * k)
    right(120)
pu()
for x in range(11):
    for y in range(11):
        goto(x*k, y*k)
        dot(4)
done()