# Элементы последовательности – четырёхзначные натуральные числа.
# Найдите все тройки элементов последовательности, для которых пятеричная
# запись суммы всех чисел тройки представляет собой палиндром,
# а среднее арифметическое всех чисел тройки больше, чем среднее
# арифметическое всех чисел в файле, кратных 31. В ответе запишите количество
# найденных троек, затем минимальную из сумм элементов таких троек.
# В данной задаче под тройкой подразумевается три идущих подряд элемента последовательности.

file = open('17-324.txt')

s = 0
i = 0
for n in file:
    n = int(n)
    if n % 31 == 0:
        s += n
        i += 1
srarifm31 = s // i

file = open('17-324.txt')
plast = int(file.readline())
last = int(file.readline())
count = 0
minn = 1000000000000000
for n in file:
    n = int(n)
    summ = (plast + last + n)
    summ5 = ''
    while summ > 0:
        summ5 = str(summ % 5) + summ5
        summ //= 5
    summ5reverse = ''.join(reversed(summ5))
    if summ5 == summ5reverse:
        if ((plast + last + n)//3) > srarifm31:
            count += 1
            minn = min(minn, plast + last + n)
    plast = last
    last = n
print(count, minn)



