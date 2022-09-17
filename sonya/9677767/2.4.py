for x in range(0,2):
    for y in range(0,2):
        for z in range(0,2):
            if ((not(z)) and x) or (x and y):
                print(x,y,z)