file = open('17.2.txt')

count = 0
maxsumm = 0

last = -1
s = 0
i = 0

for n in file:
    n = int(n)
    if last > - 1:
        if n % 2 != 0:
            s += n
            i += 1
    last = n

srarfm = s // i
print(srarfm)

file = open('17.2.txt')

plast = -1
for number in file:
    number = int(number)
    if plast > - 1:
        if (plast % 5 == 0 and number < srarfm) or (plast % 5 != 0 and plast < srarfm):
            count += 1
            summ = number + plast
            if summ > maxsumm:
                maxsumm = summ
    plast = number
print(count, maxsumm)