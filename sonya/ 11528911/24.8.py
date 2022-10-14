file = open('24.8.txt').read()

count = 0
maxcount = 0
last = ''

for char in file:
    if char == 'A':
        last = 'A'
    elif char == 'B':
        if last == 'A':
            count += 1
        else:
            last = ''
            if count > maxcount:
                maxcount = count
            count = 0
    elif char == 'C':
        last = ''
        if count > maxcount:
            maxcount = count
        count = 0
if count > maxcount:
    maxcount = count
print(maxcount)