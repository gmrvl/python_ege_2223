#(x ∨ ¬y) ∧ ¬(w ≡ z) ∧ w
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if (x or (not y)) and (not(w==z)) and w:
                    print(x,y,w,z)