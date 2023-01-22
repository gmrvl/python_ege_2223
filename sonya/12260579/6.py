from turtle import*
left(90)
k = 30

for i in range(4):
    forward(12*k)
    right(90)
right(30)
for v in range(3):
    forward(8*k)
    right(60)
    forward(8*k)
    right(120)
pu()
for x in range(0,13):
    for y in range(0,13):
        goto(x * k, y * k)
        dot(4)
done()