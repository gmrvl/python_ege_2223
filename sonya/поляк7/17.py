#Элементы последовательности – четырёхзначные натуральные числа. Найдите все тройки элементов последовательности,
# для которых все суммы пар, составленные из всех чисел тройки – точные квадраты, а наименьшая сумма пары больше,
# чем среднее арифметическое всех чисел в файле, кратных 50. В ответе запишите количество найденных троек, затем
# минимальную из сумм элементов таких троек. В данной задаче под тройкой подразумевается
# три идущих подряд элемента последовательности.
file = open('17-328.txt')
i = 0
s = 0
for n in file:
    n = int(n)
    if n % 50 == 0:
        s += n
        i += 1
srarifm = s // i

file = open('17-328.txt')
count = 0
minsumm = 1000000000000
plast = int(file.readline())
last = int(file.readline())
for n in file:
    n = int(n)
    if (n + last) ** 0.5 == int((n + last) ** 0.5) and (n + plast) ** 0.5 == int((n + plast) ** 0.5) and (plast + last) ** 0.5 == int((plast + last) ** 0.5):
        if min(n + last,n + plast,plast + last) > srarifm:
            count += 1
            minsumm = min(minsumm, n + last + plast)
    plast = last
    last = n
print(count, minsumm)
