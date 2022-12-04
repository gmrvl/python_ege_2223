file = open('17.1.txt')

count = 0
maxraz = 0
last = int(file.readline())

for n in file:
    n = int(n)
    if (abs(last - n) % 45 == 0) and (n % 18 == 0 or last % 18 == 0):
        count += 1
        raz = abs(last - n)
        if raz > maxraz:
            maxraz = raz
    last = n
print(count, maxraz)