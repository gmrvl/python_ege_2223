for x in range(0,2):
    for y in range(0, 2):
        for z in range(0, 2):
            if (x and y) or ((not(x)) and (not(z))):
                print(x,y,z)

