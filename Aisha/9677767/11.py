# ((x ∧ w) ∨ (w ∧ z)) ≡ ((z → y) ∧ (y → x))

for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (((x * w) + (w * z)) == ((z <= y) * (y <= x))) == 1:
                    print(x,y,z,w)