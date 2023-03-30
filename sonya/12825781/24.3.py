file = open('24.4.txt').read()
count = 0
maxcount = 0
for char in file:
    if char == 'X':
        count += 1
    else:
        maxcount = max(maxcount, count)
        count = 0
print(maxcount)