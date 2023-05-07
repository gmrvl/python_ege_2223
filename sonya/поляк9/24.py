file = open('24-209 (1).txt').read()
count = 0
msxcount = 0
last = ''
#АB, CB, BС и BA
for char in file:
    if last == 'A' and char == 'B':
        count += 1
    if (char == 'C' or char == 'A') and last == 'B':
        count += 1
    if char == 'B' and last == 'C':
        count += 1
    else:
        msxcount = max(msxcount, count)
        count = 0
    last = char
print(msxcount)