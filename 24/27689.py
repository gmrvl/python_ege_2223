file = open('27689.txt').read()

count = 0
maxCount = 0
last = ''

for char in file:
    if char == 'X':
        if last == '' or last == 'Z':
            count += 1
        else:
            if count > maxCount:
                maxCount = count
            count = 1
        last = char
    if char == 'Y':
        if last == 'X':
            count += 1
            last += char
        else:
            if count > maxCount:
                maxCount = count
            count = 0
            last = char
    if char == 'Z':
        if last == 'XY':
            count += 1
        else:
            if count > maxCount:
                maxCount = count
            count = 0
        last = char
if count > maxCount:
    maxCount = count
print(maxCount)
