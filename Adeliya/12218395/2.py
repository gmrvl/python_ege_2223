# ((w → ¬x) ≡ (z → y)) ∧ (y ∨ w)
for x in range(0,2):
    for y in range(0,2):
        for w in range(0,2):
            for z in range(0,2):
                if  ((w <= (not x)) == (z <= y)) and (y or w):
                    print(x,y,w,z)
