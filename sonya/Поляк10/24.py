file = open('24-212.txt').read()
count = 0
maxcount = 0
c = 0

for char in file:
    if (char == 'A' or char == 'O') and (c == 0 or c == 2):
        count += 1
        c = 1
    elif (char == 'B' or char == 'C' or char == 'D') and c == 1:
        count += 1
        c = 2
    else:
        c = 0
        maxcount = max(maxcount,count)
        count = 0
print(maxcount)