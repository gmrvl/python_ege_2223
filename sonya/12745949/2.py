for x in range(0,2):
    for y in range(0, 2):
        for z in range(0, 2):
            if not((x == y ) or ((y or z) <= x)):
                print(x,y,z)
