from turtle import*
left(90)
k = 30

for i in range(10):
    right(60)
    forward(10* k)
    right(60)
pu()
for x in range(0,12):
    for y in range(-10, 12):
        goto(x * k, y *k)
        dot(4)
done()