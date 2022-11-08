file = open('24РНО..txt').read()

count = 0
maxcount = 0
last = ''

for char in file:
    if last == 'd' and char == 'a':
        if count > maxcount:
            maxcount = count
        count = 0
    if last == 'a' and char == 'd':
        if count > maxcount:
            maxcount = count
        count = 0
    else:
        count += 1
    last = char
print(maxcount)
