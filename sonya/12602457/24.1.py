file = open('24.1.txt').read()
count = 0
maxcount = 0
last = ''
for char in file:
    if char == 'A':
        if last == 'B' or last == '':
            count += 1
        else:
            maxcount = max(maxcount, count)
            count = 1
    elif char == 'B':
        if last == 'A':
            count += 1
        else:
            maxcount = max(maxcount, count)
            count = 0
    else:
        maxcount = max(maxcount, count)
        count = 0
    last = char
print(maxcount)