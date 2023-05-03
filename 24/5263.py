file = open('5263.txt').read()
# ABEC, BDAC, CAFB, CFBA
last = ''
position = 0
max_count = 0
max_line = ''

for i in file:
    if position == 0:
        if i == 'A' or i == 'B' or i == 'C':
            last += i
            position = 1
    elif position == 1:
        l = last[-1]
        if (l == 'A' and i == 'B') or (l == 'B' and i == 'D') or (l == 'C' and i == 'F') or (l == 'C' and i == 'A'):
            last += i
            position = 2
        else:
            if i == 'A' or i == 'B' or i == 'C':
                if max_count < len(last):
                    max_count = len(last)
                    max_line = last
                last = i
                position = 1
            else:
                if max_count < len(last):
                    max_count = len(last)
                    max_line = last
                last = ''
                # max_count
                position = 0
    elif position == 2:
        l = last[-1]
        if (l == 'B' and i == 'E') or (l == 'D' and i == 'A') or (l == 'A' and i == 'F') or (l == 'F' and i == 'B'):
            last += i
            position = 3
        else:
            if (l == 'A' and i == 'B') or (l == 'B' and i == 'D') or (l == 'C' and i == 'F') or (l == 'C' and i == 'A'):
                if max_count < len(last):
                    max_count = len(last)
                    max_line = last
                last = l + i
                # max
                position = 2
            elif i == 'A' or i == 'B' or i == 'C':
                if max_count < len(last):
                    max_count = len(last)
                    max_line = last
                last = i
                # max_count
                position = 1
            else:
                if max_count < len(last):
                    max_count = len(last)
                    max_line = last
                last = ''
                # max_count
                position = 0
    elif position == 3:
        l = last[-1]
        if (l == 'E' and i == 'C') or (l == 'A' and i == 'C') or (l == 'F' and i == 'B') or (l == 'B' and i == 'A'):
            last += i
            position = 1
        elif (l == 'B' and i == 'D') or (l == 'A' and i == 'B'):
            if max_count < len(last):
                max_count = len(last)
                max_line = last
            last = l + i
            # max
            position = 2
        elif i == 'A' or i == 'B' or i == 'C':
            if max_count < len(last):
                max_count = len(last)
                max_line = last
            last = i
            # max_count
            position = 1
        else:
            if max_count < len(last):
                max_count = len(last)
                max_line = last
            last = ''
            # max_count
            position = 0
print(max_line)
print(max_count)
print(max_line.count('ABEC') + max_line.count('BDAC') + max_line.count('CAFB') + max_line.count('CFBA'))
