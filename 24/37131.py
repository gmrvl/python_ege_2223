# Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z).
# Определите наибольшую длину цепочки символов, среди которых нет символов K и L, стоящих рядом.
#
# Например, в тексте ABCAABAKLD самая длинная цепочка символов, удовлетворяющая условию— ABCAABAK, её длина равна 8.
#
# Для выполнения этого задания следует написать программу. Ниже приведён файл, который необходимо обработать с помощью данного алгоритма.

file = open('37131.txt').read()

count = 0
maxCount = 0
last = ''

for i in file:
    if i == 'K':
        if last == 'L':
            maxCount = max(maxCount, count)
            count = 1
        else:
            count += 1
    elif i == 'L':
        if last == 'K':
            maxCount = max(maxCount, count)
            count = 1
        else:
            count += 1
    else:
        count += 1
    last = i
maxCount = max(maxCount, count)

print(maxCount)
