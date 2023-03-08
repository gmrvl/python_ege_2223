file = open('r24.2.txt').read()
count = 0
maxcount = 0
for char in file:
    if char == 'D':
        count += 1
    else:
        maxcount = max(maxcount, count)
        count = 0
print(maxcount)