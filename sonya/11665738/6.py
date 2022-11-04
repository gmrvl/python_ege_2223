from turtle import*

left(90)
k = 30
for i in range(5):
    forward(7*k)
    right(120)
pu()
for x in range(-2,8):
    for y in range(-2,8):
        goto(x*k,y*k)
        dot(4)
done()