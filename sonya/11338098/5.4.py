#Автомат получает на вход четырёхзначное число (число не может начинаться с нуля). По этому числу строится новое число по следующим правилам.

#1. Складываются отдельно первая и вторая, вторая и третья, третья и четвёртая цифры заданного числа.

#2. Наименьшая из полученных трёх сумм удаляется.

#3. Оставшиеся две суммы записываются друг за другом в порядке неубывания без разделителей.

#ример. Исходное число: 1984. Суммы: 1 + 9 = 10, 9 + 8 = 17, 8 + 4 = 12.

#Удаляется 10. Результат: 1217.

#Укажите наименьшее число, при обработке которого автомат выдаёт результат 613

for i in range(1000,10000):
    n = str(i)
    a = int(n[0]) + int(n[1])
    b = int(n[1]) + int(n[2])
    c = int(n[2]) + int(n[3])
    if a < b and a < c:
        if b > c:
            n = str(c) + str(b)
        else:
            n = str(b) + str(c)
    elif b < a and b < c:
        if a > c:
            n = str(c) + str(a)
        else:
            n = str(a) + str(c)
    else:
        if a>b:
            n = str(b) + str(a)
        else:
            n = str(a) + str(b)
    if n == '613':
        print(i)