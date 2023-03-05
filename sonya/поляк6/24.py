file = open('24-215.txt').read()
count = 0
maxcount = 0
last = ''
for char in file:
    if len(last) < 3:
        last += char
    if len(last) == 3:
        if last[0] == ('1' or '2' or '3') and last[2] == ('1' or '2' or '3') and last[1] == ('A' or 'B' or 'C'):
            count += 3
            last = ''
        else:
            maxcount = max(maxcount, count)
            count = 0
            last = last[1:]
print(maxcount)