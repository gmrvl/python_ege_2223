# Найдите максимальную длину строки, состоящей только из комбинаций BAC и СAB.

file = open('5464.txt').read()

count = 0
maxCount = 0
l = ''
last = '000'

for i in file:
    if i == 'B':
        if last[1:3] == 'CA' or last == 'BAC' or last == 'CAB':
            count += 1
            l += i
        else:
            if count > maxCount:
                maxCount = count
                print(l)
            count = 1
            l = i
    if i == 'C':
        if last[1:3] == 'BA' or last == 'BAC' or last == 'CAB':
            count += 1
            l += i
        else:
            if count > maxCount:
                maxCount = count
                print(l)
            count = 1
            l = i
    if i == 'A':
        if (last[2] == 'B' or last[2] == 'C'):
            if last[1] != 'A':
                count += 1
                l += i
            else:
                if count > maxCount:
                    maxCount = count
                    print(l)
                count = 2
                l = last[2] + 'A'

        else:
            if count > maxCount:
                maxCount = count
                print(l)
            count = 0
            l = ''

    last = last[1:] + i
print(maxCount)
