file = open('17.3.txt')

counts = 0
maxsumm = 0
last = -2

for number in file:
    number = int(number)
    if last > -1:
        if (last * number) % 15 == 0:
            summ = last + number
            if summ % 7 == 0:
                counts += 1
                if summ > maxsumm:
                    maxsumm = summ
    last = number
if summ > maxsumm:
    maxsumm = summ
print(counts, maxsumm)