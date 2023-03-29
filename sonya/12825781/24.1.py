file = open('24.1.txt').readline()
file = file.replace('KL', '1')
file = file.replace('LK', '1')
count = 0
maxcount = 0
for char in file:
    if char == '1':
        count += 1
        maxcount = max(maxcount, count)
        count = 1
    else:
        count += 1
print(maxcount)