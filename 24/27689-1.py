file = open('27689.txt').read()

count = 0
maxCount = 0

c = 0
for char in file:
    if char == 'X' and (c == 3 or c == 0):
        count += 1
        c = 1
    elif char == 'Y' and c == 1:
        count += 1
        c = 2
    elif char == 'Z' and c == 2:
        count += 1
        c = 3
    else:
        if count > maxCount:
            maxCount = count
        if char == 'X':
            count = 1
            c = 1
        elif char == 'Y':
            c = 2
            count = 0
        elif char == 'Z':
            c = 3
            count = 0
if count > maxCount:
    maxCount = count
print(maxCount)

