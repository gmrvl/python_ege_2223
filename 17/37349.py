file = open('37349.txt')

count = 0
allD, del2, del13, del26 = 0, 0, 0, 0
maxAll, max26, max13, max2 = 0, 0, 0, 0

for digit in file:
    digit = int(digit)
    if digit % 13 == 0 and digit % 2 == 0:
        count += allD
        del26 += 1
        del2 += 1
        del13 += 1
        if digit > max26:
            max26 = digit
    elif digit % 13 != 0 and digit % 2 == 0:
        count += del13
        del2 += 1
        if digit > max2:
            max2 = digit
    elif digit % 13 == 0 and digit % 2 != 0:
        count += del2
        del13 += 1
        if digit > max13:
            max13 = digit
    elif digit % 13 != 0 and digit % 2 != 0:
        count += del26
    allD += 1
    if digit > maxAll and digit != max26:
        maxAll = digit
maxmax = max(maxAll + max26, max13 + max2)
print(count, maxmax)

