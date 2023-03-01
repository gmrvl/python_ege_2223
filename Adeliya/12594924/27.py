file = open('27-B_1.txt')
n = int(file.readline())
summ = 0
difference = 10**10
for line in file:
    i, j = map(int, line.split())
    summ += max(i, j)
    if (i % 5 != j % 5) and abs(i - j) < difference:
        difference = abs(i - j)

if summ % 5 == 0:
    summ -= difference
print(summ)
