for x in range(0,2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                if not((not(y <= x)) or (z <= w) or (not(z))):
                    print(x,y,z,w)
