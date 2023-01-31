file = open('24.2.txt').read()

count = 0
maxcount = 0
c = 0

for char in file:
    if char == 'A' and c == 0:
        count += 1
        c = 1
    elif char == 'B' and c == 1:
        count += 1
        c = 0
    else:
        maxcount = max(maxcount,count)
        count = 0
        c = 0
print(maxcount)