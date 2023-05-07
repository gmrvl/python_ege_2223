from turtle import*
left(90)
k = 30
for i in range(10):
    forward(5*k)
    right(60)
pu()
for x in range(12):
    for y in range(-5,10):
        goto(x*k,y*k)
        dot(4)
done()