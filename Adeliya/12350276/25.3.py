for i in range(185311,185331):
    sq=int(i**0.5)
    a=[]
    for dell in range(1,sq+1):
        if i % dell == 0:
            dell2 = i // dell
            a.append(dell)
            a.append(dell2)
            if len(a) > 4:
                break
    if len(a) == 4:
        a = sorted(a)
        print(a)


