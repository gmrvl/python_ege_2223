# ((x → y ) ∧ (y → w)) ∨ (z ≡ ( x ∨ y))


for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if (((x <= y) * (y <= w)) + (z == (x + y))) == 0:
                    print(x,y,w,z)
