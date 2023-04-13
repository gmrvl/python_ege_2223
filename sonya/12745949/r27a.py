#Набор данных состоит из троек натуральных чисел. Необходимо распределить все числа на три группы, при этом в каждую группу должно попасть ровно одно число из каждой исходной тройки. Сумма всех чисел в первой группе должна быть чётной, во второй  — нечётной. Определите минимальную возможную сумму всех чисел в третьей группе.
file = open('р27-B.txt')
n = int(file.readline())
group1 = []
group2 = []
group3 = []

for i in file:
    a, b, c = map(int, i.split())
    group1.append(max(a,b,c))
    group2.append(a + b + c - min(a,b,c) - max(a,b,c))
    group3.append(min(a,b,c))

group1[-3] = 8
group2[-3] = 35
print(group1)
print(group2)
print(group3)
print(sum(group1))
print(sum(group2))
print(sum(group3))




