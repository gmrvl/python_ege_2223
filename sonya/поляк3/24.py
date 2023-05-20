# комбинаций BAC и СAB
file = open('24-224.txt').readline()
file = file.replace('CAB', '*')
file = file.replace('BAC', '*')
print(file)
count = 0
maxcount = 0
for char in file:
    if char == '*':
        count += 1
    else:
        maxcount = max(maxcount, count)
        count = 0
maxcount = max(maxcount, count)
print(maxcount)
