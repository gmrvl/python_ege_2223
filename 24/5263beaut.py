file = open('5263.txt').read()
last, max_line = '', ''
position, max_count = 0, 0


# функция сравнения строк с максимумом
def max_l(max_count, max_line):
    if max_count < len(last):
        max_count = len(last)
        max_line = last
    return max_count, max_line


# функция, отвещающая за 0 и 1 позиции, т.к. они везде одинаковые
def position1_0(i, last, position, max_count, max_line):
    # max_count, max_line = max_l(max_count, max_line)
    if i == 'A' or i == 'B' or i == 'C':
        last = i
        position = 1
    else:
        last = ''
        position = 0
    return last, position, max_count, max_line


def position2(i, last, position, max_count, max_line):
    max_count, max_line = max_l(max_count, max_line)
    if (l == 'A' and i == 'B') or (l == 'B' and i == 'D') or (l == 'C' and i == 'F') or (l == 'C' and i == 'A'):
        last += i
        position = 2
    else:
        last, position, max_count, max_line = position1_0(i, last, position, max_count, max_line)
    return last, position, max_count, max_line


for i in file:
    if len(last) > 0: l = last[-1]
    if position == 0:
        last, position, max_count, max_line = position1_0(i, last, position, max_count, max_line)
    elif position == 1:
        last, position, max_count, max_line = position2(i, last, position, max_count, max_line)
    elif position == 2:
        if (l == 'B' and i == 'E') or (l == 'D' and i == 'A') or (l == 'A' and i == 'F') or (l == 'F' and i == 'B'):
            last += i
            position = 3
        else:
            last, position, max_count, max_line = position2(i, l, position, max_count, max_line)
    elif position == 3:
        if (l == 'E' and i == 'C') or (l == 'A' and i == 'C') or (l == 'F' and i == 'B') or (l == 'B' and i == 'A'):
            last += i
            position = 1
        else:
            last, position, max_count, max_line = position2(i, l, position, max_count, max_line)

print(max_line.count('ABEC') + max_line.count('BDAC') + max_line.count('CAFB') + max_line.count('CFBA'))
