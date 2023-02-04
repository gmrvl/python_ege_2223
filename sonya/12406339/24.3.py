file = open('zadanie24_1 (3).txt').read()
count = 0
maxcount = 0
for char in file:
    if char == 'B':
        count += 1
    else:
        maxcount = max(maxcount, count)
        count = 0
print(maxcount)