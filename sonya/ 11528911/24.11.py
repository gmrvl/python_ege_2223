file = open('24.11.txt').read()

count = 0
maxcount = 0
plast = ''
last = ''

for char in file:
    if char == 'L':
        plast = 'L'
        last = ''
    elif char == 'D':
        if plast == 'L':
            last = 'D'
        else:
            plast = ''
            if count > maxcount:
                maxcount = count
            count = 0
    elif char == 'R':
        if plast == 'L' and last == 'D':
            count += 1
            plast = ''
            last = ''
        else:
            plast = ''
            last = ''
            if count > maxcount:
                maxcount = count
            count = 0
if count > maxcount:
    maxcount = count
print(maxcount)
