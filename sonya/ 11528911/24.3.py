file = open('24.3.txt').read()

count = 0
maxcount = 0
plast = ''
last = ''

for char in file:
    if char == 'X':
        if last == 'Z' or last == '':
            count += 1
        else:
            count = 1
    elif char == 'Y':
        if last == 'X':
            count += 1
        else:
            if count > maxcount:
                maxcount = count
            count = 0
    elif char == 'Z':
        if plast == 'X' and last == 'Y':
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
