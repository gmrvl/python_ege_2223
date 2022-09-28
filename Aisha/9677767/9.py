# (¬x ∧ ¬y) ∨ (y ≡ z) ∨ ¬w

for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (((not x) *(not y)) + ( y == z) + (not w)) == 0:
                    print(x,y,z,w)