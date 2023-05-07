#Повтори 5 [Вперёд 8 Направо 60 Вперёд 8 Направо 120]
from turtle import*
left(90)
k = 30
for i in range(5):
    forward(8*k)
    right(60)
    forward(8 * k)
    right(120)
pu()
for x in range(10):
    for y in range(17):
        goto(x*k, y*k)
        dot(4)
done()