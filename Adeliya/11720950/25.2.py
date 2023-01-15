for i in range(210235, 210301):
    sq = int(i**0.5)
    a=[]
    for dell in range(2, sq):
        if i % dell == 0:
            a.append(dell)
            a.append(i//dell)
        if len(a)>4:
            break
    if len(a)==4:
        a=sorted(a)
        print(a)



