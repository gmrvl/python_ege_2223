file = open('r24.3.txt').read()
count = 0
maxcount = 0
for char in file:
    if char == 'L':
        count += 1
    else:
        maxcount = max(maxcount, count)
        count = 0
maxcount = max(maxcount, count)
print(maxcount)