file = open('39763.txt')

count = 0
max_sum = 0
a = int(file.readline())
b = int(file.readline())
for digit in file:
    c = int(digit)
    d = sorted([a, b, c])
    if d[0]**2 + d[1]**2 > d[2]**2:
        count += 1
        max_sum = max(sum(d), max_sum)
    a = b
    b = c
print(count, max_sum)