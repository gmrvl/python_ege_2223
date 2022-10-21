file = open('24.8.txt').read()

count = 0
maxcount = 0

for char in file:
    if char == 'A':
        count += 1
        if count > maxcount:
            maxcount = count
        count = 0
    else:
        count += 1
if count > maxcount:
    maxcount = count
print(maxcount)