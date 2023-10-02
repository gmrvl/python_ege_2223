file = open('24.18.txt').read()
last =''
maxcount = count = 0
for n in file:
    if len(last) < 3:
        last += n
    else:
        if (int(last[0]) + int(last[1])) > int(last[2]):
            count += 1
        else:
            maxcount = max(maxcount, count)
            count = 1
        last = last[1:] + n
print(maxcount)