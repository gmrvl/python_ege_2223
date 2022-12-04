file = open('24.1.txt').read()

last = ''
count = 0
maxcount = 0

for char in file:
    if (last == '' or last == 'L') and char == 'L':
        count += 1
    else:
        if count > maxcount:
            maxcount = count
        count = 1
    last = char
print(maxcount)