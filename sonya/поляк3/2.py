for a in range(0,2):
    for b in range(0,2):
        for c in range(0,2):
            for d in range(0,2):
                if not((a <= b) and (c <= d) or (not(c))):
                    print(a,b,c,d)