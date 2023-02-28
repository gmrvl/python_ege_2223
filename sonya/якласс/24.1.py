file = open('24.txt').readline()
count = 0
maxcount = 0
file = file.replace('AN', '1')
file = file.replace('AE', '1')
for i in range(0, len(file)):
    if file[i] == '1':
        count += 1
    else:
        maxcount = max(maxcount, count)
        count = 0
print(maxcount)