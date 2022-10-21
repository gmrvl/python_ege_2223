# Определите максимальное количество идущих подряд символов,
# среди которых каждые два соседних различны.

file = open('27421.txt').read()

last = ''
count = 0
maxCount = 0

for char in file:
    if last != char:
        count += 1
    else:
        if count > maxCount:
            maxCount = count
        count = 1
    last = char

if count > maxCount:
    maxCount = count
print(maxCount)
