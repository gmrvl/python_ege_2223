#Определите количество пар элементов последовательности, для которых в восьмеричной записи обоих чисел пары максимальная цифра расположена левее
# минимальной цифры, а сумма чисел пары меньше,
# чем среднее арифметическое всех чисел в файле, кратных 22. В ответе запишите количество найденных пар,
# затем максимальную из сумм элементов таких пар.
# В данной задаче под парой подразумевается два идущих подряд элемента последовательности.
file = open('17-340.txt')

s = 0
i = 0

for string in file:
    string = int(string)
    if string % 22 == 0:
        s += 1
        i += string
    last = string

srarifm = i // s
print(srarifm)

file = open('17-340.txt')

count = 0
maxsumm = 0
last = int(file.readline())

for n in file:
    n = int(n)
    n8 = oct(n)
    last8 = oct(last)
    m = list(n8)
    minn = min(m)
    maxx = max(m)
    l = list(last8)
    minl = min(l)
    maxl = max(l)
    if n8.find(maxx) > n8.find(minn) and last8.find(maxl) > last8.find(minl) and (last + n) < srarifm:
        count += 1
        maxsumm = max(maxsumm, last + n)
    last = n
print(count,maxsumm)



