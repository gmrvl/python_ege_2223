from itertools import*
a = product('БОРИС', repeat=6)
count = 0
for x in a:
    s = ''.join(x)
    if s.count('Б') == 1 and s.count('Р') == 1 and s.count('С') <= 1:
        count += 1
print(count)