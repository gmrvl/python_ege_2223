file = open('24.7.txt').read()

count = 0
maxcount = 0
с = 0

for char in file:
    if char == 'K':
        if с == 2:
            if count > maxcount:
                maxcount = count
            count = 0
        else:
            count += 1
        с = 1
    elif char == 'L':
        if с == 1:
            if count > maxcount:
                maxcount = count
            count = 0
        else:
            count += 1
        с = 2
    else:
        count += 1
        с = 0
if count > maxcount:
    maxcount = count
print(maxcount)