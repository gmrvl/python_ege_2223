file = open('39763.txt')

count = 0
max_pair = 0
s = int(file.readline())
n = int(file.readline())
for digit in file:
    digit = int(digit)
    a = [s, n, digit]
    b = sorted(a)
    if b[0]**2 + b[1]**2 == b[2]**2:
        count += 1
        max_pair = max(max_pair, sum(a))
    s = n
    n = digit
print(count, max_pair)
