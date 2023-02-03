import math

for i in range(2000000, 3000001):
    a = []
    stop = int(math.sqrt(i))
    for dell in range(1, stop+1):
        if i % dell == 0:
            dell2 = i // dell
            a.append(dell2 - dell)
    a = sorted(a)
    count = 0
    for x in a:
        if x <= 115:
            count += 1
        if count == 3:
            print(i)
            break
