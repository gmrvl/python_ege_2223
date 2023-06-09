file = open('24-215.txt').readline()
file = file.replace('B', 'A')
file = file.replace('C', 'A')
file = file.replace('2', '1')
file = file.replace('3', '1')
file = file.replace('A1', '0')
count = 0
maxcount = 0
for char in file:
    if char == '0':
        count += 1
    else:
        maxcount = max(maxcount, count)
        count = 0
print(maxcount)
