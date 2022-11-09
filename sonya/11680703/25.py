import math

for n in range(2_000_000, 3_000_001):
    raz = []
    stop = int(math.sqrt(n))
    for dell in range(1, stop+1):
        if n % dell == 0:
            p_dell = n // dell
            raz.append(p_dell - dell)
    raz = sorted(raz)
    count = 0
    for x in raz:
        if x <= 115:
            count += 1
        if count == 3:
            print(n)
            break



