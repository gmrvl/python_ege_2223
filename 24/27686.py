file = open('27686.txt').read()

count = 0
maxCount = 0
for char in file:
    if char == 'X':
        count += 1
    else:
        if count > maxCount:
            maxCount = count
        count = 0
if count > maxCount:
    maxCount = count
print(maxCount)
