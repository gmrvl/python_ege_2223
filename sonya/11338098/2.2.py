for x in range (0,2):
    for y in range (0,2):
        for z in range (0,2):
            for w in range (0,2):
                if (x <= y) and (y != z) and (z or w):
                    print(x,y,z,w)