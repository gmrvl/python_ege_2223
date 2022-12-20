# Определите количество пар, в которых один из двух элементов делится на 3,
# а другой меньше среднего арифметического
# всех чётных элементов последовательности.

file = open('46975.txt')
summ = 0
countChet = 0
for digit in file:
    digit = int(digit)
    if digit % 2 == 0:
        summ += digit
        countChet += 1
aver = summ // countChet  # среднее арифметическое

file = open('46975.txt')
count = 0
maxSum = 0

first = int(file.readline())
for digit in file:
    second = int(digit)
    if (first % 3 == 0 and second < aver) or (first < aver and second % 3 == 0):
        count += 1
        if first + second > maxSum:
            maxSum = first + second
    first = second

print(count, maxSum)
