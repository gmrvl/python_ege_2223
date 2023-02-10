file = open('24.3.txt').read()

maxcount = 0
count = 0
c = 0

for char in file:
    if char == 'L' and c == 0:
        count += 1
        c = 1
    elif char == 'L':
        maxcount = max(maxcount, count)
        count = 1
        c = 1
    elif char == 'D' and c == 1:
        count += 1
        c = 2
    elif char == 'R' and c == 2:
        count += 1
        c = 0
    else:
        maxcount = max(maxcount, count)
        count = 0
        c = 0
print(maxcount)