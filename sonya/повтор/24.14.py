file = open('24.14.txt').read()
k = 0
file = file.split('A')
for i in file:
    if len(i) >= 8:
        if i.count('B') == 0:
            k += 1
print(k)
