file = open('24-215.txt').readline()
file = file.replace('A', 'B')
file = file.replace('C', 'B')
file = file.replace('2', '1')
file = file.replace('3', '1')
file = file.replace('B11', '*')

count = 0
maxcount = 0
for char in file:
    if char == '*':
        count += 1
    else:
        maxcount = max(maxcount, count)
        count = 0
print(maxcount)


