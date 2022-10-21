file = open('24.8.txt').read()

count = 0
maxcount = 0
last = ''

for char in file:
    if char == 'A':
        if last == 'B' or last == '':
            count += 1
        else:
            if count > maxcount:
                maxcount = count
            count = 1
    elif char == 'B':
        if last == 'A':
            count += 1
        else:
            if count > maxcount:
                maxcount = count
            count = 0
    elif char == 'C':
        if count > maxcount:
            maxcount = count
        count = 0
    last = char
if count > maxcount:
    maxcount = count
print(maxcount)