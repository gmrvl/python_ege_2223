# Определите максимальную длину цепочки вида LDRLDRLDR...
# (составленной из фрагментов LDR, последний фрагмент может быть неполным)

file = open('27699.txt').read()

count = 0
maxCount = 0
last = 3

for i in file:
    if i == 'L':
        if last == 3:
            count += 1
        else:
            if count > maxCount:
                maxCount = count
            count = 1
        last = 1
    if i == 'D':
        if last == 1:
            count += 1
            last = 2
        else:
            if count > maxCount:
                maxCount = count
            count = 0
            last = 0
    if i == 'R':
        if last == 2:
            count += 1
        else:
            if count > maxCount:
                maxCount = count
            count = 0
        last = 3
if count > maxCount:
    maxCount = count
print(maxCount)
