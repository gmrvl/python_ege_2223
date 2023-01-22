file=open('24.txt').read()

count = 0
maxcount = 0
c = 0
for i in file:
    if i == 'A':
        if c == 2:
            if count > maxcount:
                maxcount = count
            count = 0
            c = 0
        else:
            count += 1
            c += 1
    else:
        count += 1
if count > maxcount:
    maxcount = count
print(maxcount)