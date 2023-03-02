file = open('24.txt').readline()
count = 0
maxcount = 0
file = file.replace('QR', '1')
file = file.replace('OA', '1')
for i in range(0, len(file)):
    if file[i] == '1':
        count += 1
        maxcount = max(maxcount, count)
    else:
        maxcount = max(maxcount, count)
        count = 0
print(maxcount)
#24
