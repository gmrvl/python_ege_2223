#комбинаций BAC и СAB
file = open('24.5.txt').read()

count = 0
maxcount = 0
last = '000'

for char in file:
    if char == 'A':
        if last == 'ABC' or last == 'ABB' or last == 'ACC' or last == 'ACB':
            count += 1
        else:
            maxcount = max(maxcount, count)
            count = 1
    if char == 'B':
        if last == 'BAC' or last == 'CAB' or last == 'CCA' or last == 'BCA':
            count += 1
        else:
            maxcount = max(maxcount, count)
            count = 1
    if char == 'C':
        if last == 'CBA' or last == 'BAC' or last == 'CAB' or last == 'BBA':
            count += 1
        else:
            maxcount = max(maxcount, count)
            count = 1
    last = last[1:] + char
print(maxcount)