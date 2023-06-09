file = open('09.csv')

count = 0

for line in file:
    a = list(map(int, line.split(';')))
    a = sorted(a)
    c = 0
    povtor = 0
    for i in range(0, len(a) - 1):
        if a[i] == a[i+1]:
            c += 1
            povtor = a[i]
    if c == 1:
        sum = 0
        for i in a:
            if i != povtor:
                sum += i
        ave = sum // 3
        if ave <= povtor * 2:
            count += 1
print(count)
