file = open('24.9.txt').read()

count = 0
maxcount =0
last = ''

for char in file:
    if char == last:
        if count > maxcount:
            maxcount = count
        count = 1
    else:
        count += 1
        last = char
if count > maxcount:
    maxcount = count
print(maxcount)