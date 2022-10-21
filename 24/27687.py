# Определите длину самой длинной последовательности, состоящей из символов Y.
file = open('27686.txt').read()
count = 0
maxCount = 0

for i in file:
    if i == 'Y':
        count += 1
    else:
        if count > maxCount:
            maxCount = count
        count = 0
if count > maxCount:
    maxCount = count
print(maxCount)
