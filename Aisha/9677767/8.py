# ((x → y ) ≡ (z → w)) ∨ (x ∧ w)

for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (((x <= y) == (z <= w)) + (x* w)) == 0:
                    print(x,y,z,w)