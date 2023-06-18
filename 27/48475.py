f = open("48475-b.txt")
n = int(f.readline())
numbers = [int(x) for x in f]
i = 0
k = 0
while i != n:
    for h in range(i + 1, n):
        if (numbers[i] + numbers[h]) % 3 == 0 and (numbers[i] * numbers[h]) % 4096 == 0:
            k = k + 1
    i = i + 1
    print(i)
print(k)
