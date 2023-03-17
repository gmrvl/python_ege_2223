maxx = 0

for n in range(1, 9):
    n_b = bin(n)[2:]
    if n_b[-1] == '0':
        n_b = '10' + n_b
    else:
        n_b = '1' + n_b + '01'
    r = int(n_b, 2)
    maxx = max(r, maxx)
print(maxx)
