#Вперёд 9 Направо 90
#Повтори 2 [Вперёд 3 Направо 90 Вперёд 3 Направо 270]
#Повтори 2 [Вперёд 3 Направо 90]
#Вперёд 9
from turtle import*
left(90)
k = 30
forward(9*k)
right(90)
for i in range(2):
    forward(3*k)
    right(90)
    forward(3*k)
    right(270)
for i in range(2):
    forward(3*k)
    right(90)
forward(9*k)
pu()
for x in range(15):
    for y in range(-5,15):
        goto(x*k, y*k)
        dot(4)
done()