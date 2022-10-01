s = []

for a in range(0,1000):
    for x in range(0,1000):
        for y in range(0,1000):
            if ( int(2*x) + int(3*y) < 30) or (x + y >= a):
                s.append(a)
print(max(s))