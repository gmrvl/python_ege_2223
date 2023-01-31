# комбинаций BAC и СAB
file = open('24-224.txt').read()
count = 0
maxcount = 0
last = ''

for char in file:
    if char == 'B':
        if last == 'CA':
            count += 1
            last = ''
        elif last == '':
            count += 1
            last = 'B'
        else:
            if maxcount < count:
                maxcount = count
            count = 1
            last = 'B'
    elif char == 'C':
        if last == 'BA':
            count += 1
            last = ''
        elif last == '':
            count += 1
            last = 'C'
        else:
            if maxcount < count:
                maxcount = count
            count = 1
            last = 'C'
    elif char == 'A' and (last == 'C' or last == 'B'):
        count += 1
        last += 'A'
    else:
        maxcount = max(maxcount, count)
        count = 0
        last = ''
maxcount = max(maxcount, count)
print(maxcount)
