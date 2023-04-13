file = open('р24.2.txt').read()

count = 0
maxcount = 0
c = 0

for char in file:
    if char == 'L' and (c == 0 or c == 3):
        count += 1
        c = 1
    elif char == 'D' and c == 1:
        count += 1
        c = 2
    elif char == 'R' and c == 2:
        count += 1
        c = 3
    else:
        maxcount = max(maxcount, count)
        count = 0
        c = 0
print(maxcount)
