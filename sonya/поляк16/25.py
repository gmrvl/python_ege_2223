ch = '02468'
nch = '13579'
ns = []
for n in range(4023, 10**7, 4023):
    n = str(n)
    if len(n) == 7:
        if n[0] == '1':
            if n[1] in ch and n[3] in ch and n[5] in ch:
                if n[2] in nch and n[4] in nch and n[6] in nch:
                    print(n, int(n) // 4023)
