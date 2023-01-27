# комбинаций BAC и СAB
file = open('24-224.txt').read()
count = 0
maxcount = 0
c = 0  # bac
b = 0  # cab
last = ''

for char in file:
    if char == 'B':
        if last == 'CA' or '':
            count += 1
            last = ''
        else:
            if maxcount < count:
                maxcount = count
            count = 1
            last = 'B'

    elif char == 'C':
        if last == 'BA' or '':
            count += 1
            last = ''
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
    print(last)
print(maxcount)
