file = open('24-221.txt').read()

maxcount = 0
count = 0
pos = 0
line = ''
maxline = ''
for char in file:
    if char == '0' and pos != 1:
        count += 1
        line += char
        pos = 10
    elif char == '1' and pos != 0:
        count += 1
        line += char
        pos = 1
    else:
        if count > maxcount and pos == 1:
            maxcount = count
            maxline = line
        if char == '0':
            count = 1
            pos = 10
            line = '0'
        else:
            count = 0
            pos = 0
            line = ''
print(maxcount, maxline, len(maxline))
