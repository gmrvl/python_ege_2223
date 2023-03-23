file = open('24.6.txt').read()
count = 0
maxcount = 0
c = 0
for char in file:
    if char == 'A':
        if c >= 3:
            maxcount = max(maxcount, count)
        count = 0
        c = 0
    elif char == 'E':
        c += 1
        count += 1
    else:
        count += 1
print(maxcount)
