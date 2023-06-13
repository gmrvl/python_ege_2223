file = open('27689.txt').read()

count = 0
line = ''
max_count = 0
max_line = ''
last = ''

for char in file:
    if char == 'X':
        if last == 'Z':
            count += 1
            line += char
        else:
            if count > max_count:
                max_count = count
                max_line = line
            line = 'X'
            count = 1
    elif char == 'Y':
        if last == 'X':
            count += 1
            line += char
        else:
            if count > max_count:
                max_count = count
                max_line = line
            line = ''
            count = 0
    elif char == 'Z':
        if last == 'Y':
            count += 1
            line += char
        else:
            if count > max_count:
                max_count = count
                max_line = line
            count = 0
            line = ''
    last = char
print(max_count, max_line, len(max_line))
