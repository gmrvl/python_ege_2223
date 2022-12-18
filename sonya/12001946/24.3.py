file = open('24.3.txt').read()

count = 0
maxcount = 0

for char in file:
    if char == 'X':
        count += 1
    else:
        if count > maxcount:
            maxcount = count
        count = 0
    last = char
if count > maxcount:
    maxcount = count
print(maxcount)
