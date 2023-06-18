file = open('24.12.txt').read()
maxcount = 0
count = 0
c = 0
for char in file:
    if char == 'A' and c == 0:
        count += 1
        c = 1
    elif char == 'A' and c == 1:
        maxcount = max(maxcount, count)
        count = 0
        c = 0
    else:
        count += 1
        c = 0
print(maxcount)