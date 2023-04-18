file = open('24.2.txt').readline()
file = file.replace('ad','1')
file = file.replace('da','1')
count = 0
maxcount = 0
for char in file:
    if char != '1':
        count += 1
    else:
        maxcount = max(maxcount, count)
        count = 0
print(maxcount + 2)
