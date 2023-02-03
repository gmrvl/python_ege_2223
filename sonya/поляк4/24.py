file = open('24-223.txt').read()


last = '000'
count = 0
maxcount = 0
# AB СAС СAС
# СAС AB AB
for char in file:
    if char == 'C':
        if last == 'CAB' or last == 'BAB' or last == 'CAC' or last == 'CCA' or last == 'BCA':
            count += 1
        else:
            maxcount = max(maxcount, count)
            count = 1
    if char == 'A':
        if last == 'CAB' or last == 'BAB' or last == 'CAC' or last == 'ACC' or last == 'ABC':
            count += 1
        else:
            maxcount = max(maxcount, count)
            count = 1
    if char == 'B':
        if last == 'ABA' or last == 'ACA':
            count += 1
        else:
            maxcount = max(maxcount, count)
            count = 1
    last = last[1:] + char
print(maxcount)
