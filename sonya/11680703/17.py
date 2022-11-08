file = open('17.txt')

plast = ''
last = ''
summ = 0
maxsumm = 0
count = 0

for string in file:
    if plast != '' and last != '':
        if (int(last))**2 == (int(plast))**2 + (int(string))**2 or (int(plast))**2 == (int(last))**2 + (int(string))**2 or (int(string))**2 == (int(plast))**2 + (int(last))**2:
            count += 1
            summ = int(string) + int(last) + int(plast)
            if summ > maxsumm:
                maxsumm = summ
            summ = 0
    plast = last
    last = string
print(count, maxsumm)