for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range (2):
                if (((x and (not y)) == (z or (not w))) <= (x and z)) == 0:
                    print (x,y,z,w)