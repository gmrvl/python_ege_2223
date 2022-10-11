#  максимальное количество идущих подряд символов, среди которых каждые два соседних различны

file = open('27421.txt').read()

count = 0
maxCount = 0
last = ''

for char in file:
    if char == last:
        if count > maxCount:
            maxCount = count
        count = 1
    else:
        count += 1
    last = char
if count > maxCount:
    maxCount = count
print(maxCount)
