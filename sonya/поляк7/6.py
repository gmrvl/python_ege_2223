from turtle import*

k = 30
for i in range(6):
    left(120)
    forward(6*k)
pu()
for x in range(-7,2):
    for y in range(-7,10):
        goto(x*k,y*k)
        dot(4)
done()