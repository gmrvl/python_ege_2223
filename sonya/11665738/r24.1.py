file = open('r24.1.txt').read()

count = 0
maxcount = 0
s = 0

for char in file:
    if char == 'C' or char == 'F' or char == 'D':
        if s == 1:
            maxcount = max(maxcount, count)
            count = 0
        s = 1
    if char == 'A' or char == 'O':
        if s == 1:
            count += 1
        else:
            maxcount = max(maxcount, count)
            count = 0
        s = 0
print(maxcount)