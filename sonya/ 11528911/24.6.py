file = open('24.6.txt').read()

count = 0
maxcount = 0

for char in file:
    if char == 'B':
        count += 1
    else:
        if count > maxcount:
            maxcount = count
        count = 0
if count > maxcount:
    maxcount = count
print(maxcount)