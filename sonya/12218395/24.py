file = open('24.txt').readline()

count = 0
maxcount = 0
c = 0
for char in file:
    if char == 'A':
        if c == 2:
            maxcount = max(maxcount, count)
            count = 0
            c = 0
        else:
            count += 1
        c += 1
    else:
        count += 1
print(maxcount)
