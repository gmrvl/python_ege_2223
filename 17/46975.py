# Определите количество пар, в которых один из двух элементов делится на 3,
# а другой меньше среднего арифметического
# всех чётных элементов последовательности.

file = open('46975.txt')
summ = 0
count = 0
for digit in file:
    digit = int(digit)
    if digit % 2 == 0:
        summ += digit
        count += 1
aver = summ // count # среднее арифметическое

file = open('46975.txt')
count = 0

first = int(file.readline())
for digit in file:
    second = int(digit)
    if (first % 3 == 0 and second < aver) or (first < aver and second % 3 == 0):
        count +=1

print(count)

