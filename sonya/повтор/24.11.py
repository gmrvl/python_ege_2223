file = open('24.11.txt').read()
maxcount = 0
count = 0
c =0
for char in file:
    if char == 'P' and c == 0:
        count += 1
        c = 1
    elif char == 'P' and c == 1:
        maxcount = max(maxcount, count)
        count = 1
        c = 1
    else:
        count += 1
        c = 0
print(maxcount)