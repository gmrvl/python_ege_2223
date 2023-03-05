file = open('24.2.txt').readline()
file = file.replace('L', '1')
file = file.replace('K', '1')
count = 0
maxcount = 0
last = ''
for char in file:
    if last == char:
        maxcount = max(maxcount, count)
        count = 1
    else:
        count += 1
    last = char
print(maxcount)