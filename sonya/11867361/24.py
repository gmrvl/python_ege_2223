file = open('zadanie24_1.txt').read()
count = 0
maxcount = 0
last = ''
for char in file:
    if (last == '' or last == 'A') and char == 'A':
        count += 1
    else:
        if count > maxcount:
            maxcount = count
        count = 1
    last = char
if count > maxcount:
    maxcount = count
count = 0
print(maxcount)