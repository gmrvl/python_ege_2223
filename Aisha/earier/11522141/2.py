# ¬((x ∨ y) → (z ∧ w)) ∧ (x → w)

for x in range (2):
    for y in range (2):
        for z in range (2):
            for w in range (2):
                if (not((x or y) <= (z and w)) and (x <= w)) == 1:
                    print(x,y,z,w)