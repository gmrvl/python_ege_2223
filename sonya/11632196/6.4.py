from turtle import*
left(126)
k = 30
for i in range(6):
    right(36)
    forward(10*k)
    right(36)
pu()
for x in range(-4, 17):
    for y in range(-4, 17):
        goto(x*k, y*k)
        dot(4)
done()