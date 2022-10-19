file = open('24.12.txt').read()

count = 0
maxcount = 0
last = ''

for char in file:
    if char == 'C' or char == 'D' or char == 'F':
        last = 'c'
    elif char == 'A' or char == 'O':
        if last == 'c':
            count += 1
            last = ''
        else:
            last = ''
            if count > maxcount:
                maxcount = count
            count = 0
if count > maxcount:
    maxcount = count
print(maxcount)

