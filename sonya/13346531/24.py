file = open('24.txt').readline()
file = file.replace('Q', 'S')
file = file.replace('R', 'S')

c = 0
count = 0
maxcount = 0
for char in file:
    if char == 'S' and c == 0:
        count += 1
        c = 1
    elif char == 'S' and c == 1:
        maxcount = max(maxcount, count)
        count = 1
        c = 1
    else:
        count += 1
        c = 0
maxcount = max(maxcount, count)
print(maxcount)
