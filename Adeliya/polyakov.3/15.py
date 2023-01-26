def Del(x,y):
    return x%y==0
def f(x,a):
    return (Del(x,2) <= (not Del(x, 3))) or ((x + a) >= 80)
for a in range(1,100):
    ok=True
    for x in range(0,100):
        if not f(x,a):
            ok=False
            break
    if ok:
        print(a)
        break
