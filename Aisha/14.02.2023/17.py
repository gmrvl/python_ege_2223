file = open('17.txt')

count = 0
max_pair = 0

a = []
for digit in file:
    a.append(int(digit))

for i in range(0, len(a) - 1):
    for j in range(i + 1, len(a)):
        ras = abs(a[i] - a[j])
        if ras % 60 == 0:
            count += 1
            if ras > max_pair:
                max_pair = ras
print(max_pair, count)