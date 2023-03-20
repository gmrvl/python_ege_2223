# ((¬z ∨ w) ∧ (¬x ≡ y))→(x∧z)

for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if ((((not z) or w) * ((not x) == y)) <= (x * z)) == 0:
                    print(z, w, y, x)
