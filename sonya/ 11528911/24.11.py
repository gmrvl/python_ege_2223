file = open('24.11.txt').read()

count = 0
maxcount = 0
plast = ''
last = ''

for char in file:
    if char == 'L':
        if last == 'R' or last == '':
            count += 1
        else:
            if count > maxcount:
                maxcount = count
            count = 1
    elif char == 'D':
        if last == 'L':
            count += 1
        else:
            if count > maxcount:
                maxcount = count
            count = 0
    elif char == 'R':
        if plast == 'L' and last == 'D':
            count += 1
        else:
            if count > maxcount:
                maxcount = count
            count = 0
    plast = last
    last = char
if count > maxcount:
    maxcount = count
print(maxcount)
