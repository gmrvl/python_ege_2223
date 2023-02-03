# Найдите максимальную длину строки, состоящей только из комбинаций BAC и СAB.

file = open('24-224.txt').read()

count = 0
maxCount = 0

number = 0
last = '000'

# BAC CAB

for i in file:
    if i == 'C':
        if number == 0 or number == 3:
            number = 4
            count += 1
        elif number == 2:
            number = 3
            count += 1
        else:
            number = 4
            maxCount = max(count, maxCount)
            count = 1
    if i == 'B':
        if number == 0 or number == 3:
            number = 1
            count += 1
        elif number == 5:
            number = 0
            count += 1
        else:
            number = 1
            maxCount = max(count, maxCount)
            count = 1
    if i == 'A':
        if number == 1:
            number = 2
            count += 1
        elif number == 4:
            number = 5
            count += 1
        else:
            number = 0
            maxCount = max(count, maxCount)
            count = 0
maxCount = max(count, maxCount)
print(maxCount)
# потеряли ровно 1 тройку

for i in file:
    if i == 'B':
        if last[1:] == 'CA' or last == 'BAC' or last == 'CAB':
            count += 1
        else:
            if count > maxCount:
                maxCount = count
            count = 1
    if i == 'C':
        if last[1:] == 'BA' or last == 'BAC' or last == 'CAB':
            count += 1
        else:
            if count > maxCount:
                maxCount = count
            count = 1
    if i == 'A':
        if last[2] == 'B' or last[2] == 'C':
            if last[1] != 'A':
                count += 1
            else:
                if count > maxCount:
                    maxCount = count
                count = 2
        else:
            if count > maxCount:
                maxCount = count
            count = 0
    last = last[1:] + i
print(maxCount)