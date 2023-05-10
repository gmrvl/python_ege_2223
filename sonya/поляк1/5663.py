#задание25
from fnmatch import*
a = []
for i in range(1,1000000, 500):
    a.append(i)
count = 0
for i in range(161, 17000001, 161):
    if fnmatch(str(i), '*1?*?68*'):
        count += 1
        if count in a:
            print(i, i //161, count)
