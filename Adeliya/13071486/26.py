file=open('26.txt')
n, s = map(int, file.readline().split())
a, b = [], []
for i in file:
    price, k, typ = i.split()
    price = int(price)
    if typ == 'A':
        a.append(price)
    else:
        b.append(price)
