file = open('24.3.txt').read()

count = 0
maxcount = 0
plast = ''
last = ''

for char in file:
    if char == 'X':
        plast = 'X'
        last = ''
    elif char == 'Y':
        if plast == 'X':
            last = 'Y'
        else:
            plast = ''
            if count > maxcount:
                maxcount = count
            count = 0
    elif char == 'Z':
        if plast == 'X' and  last == 'Y':
            count +=1
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