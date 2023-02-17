file = open('r24.2.txt').read()
count = 0
maxcount = 0
last = ''
for char in file:
    if len(last)< 2:
        last += char
    if len(last) == 2:
        if last[0] != last[1]:
            count += 1
        else:
            maxcount = max(maxcount, count)
            count = 1
        last = last[1:] + char
print(maxcount)