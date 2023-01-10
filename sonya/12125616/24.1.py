file = open('24.1.txt').read()

maxcount = 0
count = 0
c = 0

for char in file:
    if char == 'X' and (c == 0 or c == 3):
        count += 1
        c = 1
    elif char == 'Y' and c == 1:
        count += 1
        c = 2
    elif char == 'Z' and c == 2:
        count += 1
        c = 3
    else:
        if count > maxcount:
            maxcount = count
        count = 0
        c = 0
print(maxcount)
