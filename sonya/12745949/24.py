file = open('24.txt').readline()
count = 0
maxcount = 0
file = file.replace('ad', '1')
file = file.replace('da', '1')
for char in file:
    if char == '1':
        count += 1
        maxcount = max(maxcount, count)
        count = 1
    else:
        count += 1
print(maxcount)