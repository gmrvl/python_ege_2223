file = open('24-211.txt').readline()
file = file.replace('BE', '1')
file = file.replace('DA', '2')
file = file.replace('AF', '3')
file = file.replace('FB', '4')
print(file)
count = 0
maxcount = 0
plast = ''
last = ''
k = 0
for char in file:
    if k % 2 == 0:
        if plast == 'A' and last == '1' and char == 'C':
            count += 1
            k += 1
        elif plast == 'C' and last == '3' and char == 'B':
            count += 1
            k += 1
        elif plast == 'B' and last == '2' and char == 'C':
            count += 1
            k += 1
        elif plast == 'C' and last == '4' and char == 'A':
            count += 1
            k += 1
        else:
            maxcount = max(maxcount, count)
            count = 0
    plast = last
    last = char
print(maxcount)

