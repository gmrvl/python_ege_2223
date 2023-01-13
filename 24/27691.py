file = open('27691.txt').read()
# максимальное количество идущих подряд символов A.
count = 0
maxCount = 0

for char in file:
    if char == 'A':
        count += 1
    else:
        if count > maxCount:
            maxCount = count
        count = 0

print(maxCount)

