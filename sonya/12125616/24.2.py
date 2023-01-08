file = open('24.2.txt').read()

maxcount = 0
count = 0

for char in file:
    if char == 'Y':
        count += 1
    else:
        if count > maxcount:
            maxcount = count
        count = 0
print(maxcount)
