file = open('24.txt').read()
count = 0
maxcount = 0
c = 0
for char in file:
    if char == 'F':
        count = 0
        c = 0
    if char == 'E':
        c += 1
        if c == 1:
            count += 1
        if c == 2:
            count += 1
            maxcount = max(maxcount, count)
            count = 1
            c = 1
    else:
        count += 1
print(maxcount)
