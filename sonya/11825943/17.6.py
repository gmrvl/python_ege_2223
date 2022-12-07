file = open('17.6.txt')

last = 2
maxtri = 0
maxsumm = 0
count = 0

for i in file:
    i = int(i)
    if i % 10 == 3:
        if i > maxtri:
            maxtri = i

file = open('17.6.txt')

for n in file:
    n = int(n)
    if (((last % 10 == 3) or (last % 10 == -3)) and ((n % 10 != 3) or (n % 10 != -3))) or (((n % 10 == 3) or (n % 10 == -3)) and ((last % 10 != 3) or (last % 10 != -3))):
        summ = last ** 2 + n ** 2
        if summ >= maxtri:
            count += 1
            if summ > maxsumm:
                maxsumm = summ
    last = n
print(maxtri, count, maxsumm)

