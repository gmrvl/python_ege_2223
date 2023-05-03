file = open('24.txt').readline()
file = file.replace('Q', '*')
file = file.replace('R', '*')
file = file.replace('S', '*')

count = 0
maxcount = 0
last = ''
for char in file:
    if char == '*' and last == '*':
        maxcount = max(maxcount, count)
        count = 1
    else:
        count += 1
    last = char
print(maxcount)