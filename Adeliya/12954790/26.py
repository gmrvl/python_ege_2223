file = open('26.txt')
n, s = map(int, file.readline().split())
a, b = [], []
for i in file:
    price, typ = i.split()
    price = int(price)
    if typ == 'A':
        a.append(price)
    else:
        b.append(price)
a = sorted(a)
b = sorted(b)
print(a)
print(b)