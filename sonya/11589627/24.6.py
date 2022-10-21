file = open('24.6.txt').read()

count = 0
maxcount = 0
с = 0

for char in file:
    if char == 'X':
        с = 1
        count += 1
    elif char == 'Z':
        if с == 1:
            с = 2
        elif с == 2:
            с = 3
        count += 1
    elif char == 'Y':
        if с == 3:
            if count > maxcount:
                maxcount = count
            count = 0
        else:
            count += 1
        с = 4
if count > maxcount:
    maxcount = count
print(maxcount)