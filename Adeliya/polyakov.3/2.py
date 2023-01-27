# ((w → y) ∧ (¬ x → z)) → ((z ≡ w) ∨ (y ∧ ¬ x))
for x in range(0,2):
    for y in range(0,2):
        for w in range(0,2):
            for z in range(0,2):
                if not ((w <= y) and (not x <= z)) <= ((z==w) or (y and not x)):
                    print(x,y,w,z)