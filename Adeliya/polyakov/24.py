file = open('24.txt').read()
count = 0
maxcount = 0
last = ''
for i in file:
    if (last == 'Q') and (i == 'W'):
        if count > maxcount:
            maxcount = count
        count = 0
    count += 1
    last = i
if count > maxcount:
    maxcount = count
print(maxcount)
