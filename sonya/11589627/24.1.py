file = open('24.1.txt').read()

count = 0
maxcount = 0
last = ''

for char in file:
    if last == char:
        if count > maxcount:
            maxcount = count
        count = 1
    else:
        count += 1
    last = char
if count > maxcount:
    maxcount = count
print(maxcount)