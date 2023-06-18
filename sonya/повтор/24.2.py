file = open('24.2.txt').read()
c = 0
count = 0
maxcount = 0
for char in file:
    if char == 'X' and c == 0:
        count += 1
        c = 1
    elif char == 'Y' and c == 1:
        count += 1
        c = 2
    elif char == 'Z' and c == 2:
        count += 1
        c = 0
    else:
        maxcount = max(maxcount, count)
        count = 0
        c = 0
print(maxcount)