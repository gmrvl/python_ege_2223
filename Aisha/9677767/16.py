# (w→y) ∧ (¬y ≡ x) ∧ (x ∨ z)

for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if ((w <= y) and ((not y) == x) and (x or z)) == 1:
                    print(x, y, w, z)
