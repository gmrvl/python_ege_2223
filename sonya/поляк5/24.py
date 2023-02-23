file = open('24-222.txt').read()
count = 0
maxcount = 0
last = ''
c = 0
for char in file:
    if len(last) < 3:
        last += char
    if len(last) == 3:
        if last[0] == last[2] == 'A' and (c == 0 or c == 2) and last[1] != 'A':
            count += 1
            c = 1
        elif last[1] == 'A' and c == 1 and last[0] != 'A' and last[2] != 'A':
            count += 1
            c = 2
        else:
            maxcount = max(maxcount, count)
            count = 0
            c = 0
        last = last[1:] + char
print(maxcount)