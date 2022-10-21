file = open('24.10.txt').read()

count = 0
maxcount = 0
c = 0

for char in file:
    if char == 'A' or char == 'C':
        c = 1
    elif char == 'B':
        if c == 1:
            count += 1
        else:
            if count > maxcount:
                maxcount = count
            count = 0
        c = 2
if count > maxcount:
    maxcount = count
print(maxcount)
