prost = []
for n in range(1411111111, 1411211111):
    sqn = int(n**0.5)
    dells = 0
    for dell in range(2,sqn+1):
        if n % dell == 0:
            dells += 1
            if dells > 0:
                break
    if dells == 0:
        prost.append(n)

n = 1411111111 + 1
count = 0
while count < 5:
    if n in prost:
        prostn = []
        n = str(n)
        for x in range(0,10):
            for y in range(0,10):
                s = n
                s[x] = n[y]
                s[y] = n[x]
                sqns = int(int(s)**0.5)
                dellss = 0
                for dell in range(2,sqns + 1):
                    if s % dell == 0:
                        dellss += 1
                        if dellss > 0:
                            break
                if dellss == 0:
                    prostn.append(int(s))
        if len(prostn) >= 12:
            print(n, max(prostn))
            count += 1