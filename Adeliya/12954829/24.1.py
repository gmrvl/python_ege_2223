file=open('24.1.txt').read()
count=0
maxCount=0
last = ''

for i in file:
    if i == 'X':
        if last == '' or last == 'Z':
            count += 1
        else:
            if count > maxCount:
                maxCount = count
            count = 1
        last=i
    if i == 'Y':
        if last == 'X':
            count += 1
            last += i
        else:
            if count > maxCount:
                maxCount = count
            count = 0
            last=i
    if i == 'Z':
        if last == 'XY':
            count += 1
        else:
            if count > maxCount:
                maxCount = count
            count = 0
        last = i
if count > maxCount:
    maxCount = count
print(maxCount)
