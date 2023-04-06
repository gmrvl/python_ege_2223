#Повтори 4 [Вперёд 12 Направо 90]
#Повтори 3 [Вперёд 12 Направо 120]
from turtle import *
left(90)
k = 30
for i in range(4):
    forward(12 * k)
    right(90)
for i in range(3):
    forward(12 * k)
    right(120)
pu()
for x in range(15):
    for y in range(15):
        goto(x * k, y * k)
        dot(4)
done()