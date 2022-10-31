file = open('24.6.txt').read()

count = 0
maxcount = 0
c = 0

for char in file:
    if char == 'X':
        c = 1
        count += 1
    elif char == 'Z':
        if c == 1:
            c = 2
        elif c == 2:
            c = 3
        count += 1
    elif char == 'Y':
        if c == 3:
            if count > maxcount:
                maxcount = count
            count = 0
        else:
            count += 1
        c = 4
if count > maxcount:
    maxcount = count
print(maxcount)