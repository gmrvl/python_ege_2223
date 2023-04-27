file = open('24-212 (1).txt').readline()
file = file.replace('B', 'C')
file = file.replace('D', 'C')
file = file.replace('O', 'A')
file = file.replace('CA', '8')
count = 0
maxcount = 0
for char in file:
    if char == '8':
        count += 1
    else:
        maxcount = max(maxcount, count)
        count = 0
print(maxcount)
