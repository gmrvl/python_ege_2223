file = open('inf_22_10_20_27a.txt')
n = int(file.readline())
minsumm = 0
ost1 = 20000000
ost2 = 20000000
ost11 = 20000000
ost22 = 20000000
for i in file:
    a, b = i.split('  ')
    a = int(a)
    b = int(b)
    minsumm += min(a,b)
    if min(a,b) % 3 == 1:
        ost1 = min(a,b)
    elif max(a,b) % 3 == 1:
        ost1 = max(a, b)
    if min(a,b) % 3 == 2:
        ost1 = min(a,b)
    elif max(a,b) % 3 == 2:
        ost1 = max(a, b)
    ost11 = min(ost1, ost11)
    ost22 = min(ost22, ost2)
if minsumm % 3 == 1:
    print(minsumm - ost1)
elif minsumm % 3 == 2:
    print(minsumm - ost2)
else:
    print(minsumm)
