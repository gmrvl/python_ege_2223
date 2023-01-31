file = open('24.4.txt').read()

maxcount = 0
count = 0
s = 0


for char in file:
    if char == 'C' or char == 'D' or char == 'F':
        s = 1
    elif char == 'A' or char == 'O':
        if s == 1:
            count += 1
            s = 0
        else:
            maxcount = max(maxcount, count)
            count = 0
            s = 0
maxcount = max(maxcount, count)
print(maxcount)