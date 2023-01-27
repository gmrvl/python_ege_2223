# Найдите максимальную длину строки, состоящей только из комбинаций BAC и СAB.

file = open('5464.txt').read()

count = 0
maxCount = 0

number = 0
last = ''

# BAC CAB

for i in file:
    if i == 'C':
        if number == 0 or number == 3 or number == 6:
            number = 1
            count += 1
        elif number == 5:
            number = 6
            count += 1
        else:
            number = 1
            maxCount = max(count, maxCount)
            count = 1
    if i == 'B':
        if number == 0 or number == 3 or number == 6:
            number = 4
            count += 1
        elif number == 2:
            number = 3
            count += 1
        else:
            number = 4
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

print(maxCount)
# потеряли ровно 1 тройку
