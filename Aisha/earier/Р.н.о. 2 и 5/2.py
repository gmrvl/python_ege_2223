# ((x ∧ ¬y) ∨ (w → z)) ≡ (z ≡ x)

for x in range (2):
    for y in range (2):
        for w in range(2):
            for z in range(2):
                if(((x * (not y)) + (w <= z)) == (z == x)) == 1:
                    print (x, y, w, z)
