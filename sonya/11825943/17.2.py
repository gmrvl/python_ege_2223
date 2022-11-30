file = open('17.2.txt')

last = 2
counts = 0
maxsumm = 0


for number in file:
    number = int(number)
    if last % 3 == 0 or number % 3 == 0:
        summ = last + number
        if summ % 5 == 0:
            counts += 1
            if summ > maxsumm:
                maxsumm = summ
    last = number
if summ > maxsumm:
    maxsumm = summ
print(counts, maxsumm)