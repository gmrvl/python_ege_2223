file = open('27-B.txt')
n = int(file.readline())
lefts = [0 for i in range(1111)]
count = 0
summ = 0
for n in file:
    n = int(n)
    summ += n
    d = summ % 1111
    if summ % 1111 == 0:
        count += 1
    count += lefts[d]
    lefts[d] += 1
print(count)