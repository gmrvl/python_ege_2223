file = open('r24.2.txt').read()

count = 0
maxcount = 0
s = 0
for char in file:
    if char == 'P':
        if s == 0:
            count += 1
        if s == 1:
            maxcount = max(maxcount, count)
            count = 1
        s = 1
    else:
        count += 1
        s = 0
print(maxcount)