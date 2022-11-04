file = open('24.2.txt').read()

count = 0
maxcount = 0
last = ''

for char in file:
    if char == 'R':
        count += 1
    else:
        if count > maxcount:
            maxcount = count
        count = 0
print(maxcount)