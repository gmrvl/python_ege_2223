file = open('24.5.txt').read()
count = 0
maxcount = 0
last = ''
for char in file:
    if char != last:
        count += 1
    else:
        maxcount = max(maxcount, count)
        count = 1
    last = char
print(maxcount)