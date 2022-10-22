chdelitel = []
for delitel in range(1,100000):
    if delitel % 2 == 0:
        chdelitel.append(delitel)

d = 0
for i in range(95632,95700):
    for a in chdelitel:
        if i % a:
            d += 1
        if d == 6:
            print(i)