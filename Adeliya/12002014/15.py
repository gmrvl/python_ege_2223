# x&25 ≠ 0 → (x&9 = 0 → x&А ≠ 0)
def f(x,a):
    return (x&25 != 0) <= ((x&9 == 0) <= (x&a != 0))
for a in range(1,1000):
    ok=True
    for x in range(0,1000):
        if not f(x,a):
            ok=False
            break
    if ok:
        print(a)
        break


